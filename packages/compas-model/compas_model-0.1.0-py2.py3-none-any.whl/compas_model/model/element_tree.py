from compas.datastructures import Tree
from compas_model.model.element_node import ElementNode
from compas_model.model.group_node import GroupNode


class ElementTree(Tree):
    """A data-structure that stores a tree of elements and group nodes.

    Parameters
    ----------
    model : :class:`compas_model.model.Model`
        Model object to update the element dictionary and the graph.
    name : str, optional
        A name or str(``uuid.uuid4()``).

    Attributes
    ----------
    model : :class:`compas_model.model.Model`
        Parent class of the ElementTree that allows to access elements dict, and interactions.
    number_of_elements : int
        Number of elements only in :class:`compas_model.model.ElementNode`.

    """

    DATASCHEMA = None

    @property
    def __data__(self):
        nodes = []
        for child in self.root.children:
            nodes.append(child.__data__)

        return {
            "name": self.name,
            "nodes": nodes,
        }

    @classmethod
    def __from_data__(cls, data):
        model_tree = cls(model=None, name=data["name"])
        nodes = []

        for node in data["nodes"]:
            if "children" in node:
                nodes.append(GroupNode.__from_data__(node))
            else:
                nodes.append(ElementNode.__from_data__(node))

        for node in nodes:
            node._tree = model_tree
            node._parent = model_tree.root
            model_tree.root._children.append(node)
        return model_tree

    def __init__(self, model=None, name="root"):
        super(ElementTree, self).__init__(name=name)

        # --------------------------------------------------------------------------
        # There is only one root node and it is of type GroupNode.
        # From this node, we can backtrack to node->ElementTree->Model.
        # --------------------------------------------------------------------------
        self._root = GroupNode(name="root", geometry=None, parent=None)
        self._root._tree = self

        # --------------------------------------------------------------------------
        # Initialize the main properties of the model.
        # --------------------------------------------------------------------------
        self.name = name  # The name of the tree.
        self._model = model  # The variable that points to the model class.

    def __repr__(self):
        return "ElementTree with {} nodes".format(len(list(self.nodes)))

    def __str__(self):
        return self.__repr__()

    # ==========================================================================
    # Attributes
    # ==========================================================================

    @property
    def model(self):
        return self._model

    @property
    def number_of_elements(self):
        count = 0

        def _count_elements(node, count):
            for child in node.children:
                if isinstance(child, ElementNode):
                    count += 1
                else:
                    count = _count_elements(child, count)
            return count

        count = _count_elements(self.root, count)
        return count

    # ==========================================================================
    # Printing
    # ==========================================================================

    def print(self):
        """Print the sub-nodes in a readable format."""

        def _print(node, depth=0):
            parent_name = "None" if node.parent is None else node.parent.name
            print("-" * 100)
            message = (
                "    " * depth
                + str(node)
                + " "
                + "| Parent: "
                + parent_name
                + " | Root: "
                + node.tree.name
            )

            if depth == 0:
                message += (
                    " | Elements: " + "{" + str(node.tree.number_of_elements) + "}"
                )

            print(message)

            if node.children is not None:
                for child in node.children:
                    _print(child, depth + 1)

        _print(self.root)

    # ==========================================================================
    # Behavior - Tree
    # ==========================================================================

    def add_group(self, name=None, geometry=None, parent=None):
        """Add a :class:`compas_model.model.GroupNode` to the tree.

        Parameters
        ----------
        name : str, optional
            A name or identifier for the node.
        geometry : Any, optional
            Geometry or any other property, when you want to give a group a shape besides name.
        parent : :class:`compas_model.model.GroupNode`, optional
            The parent node of this node.

        Returns
        -------
        :class:`compas_model.model.GroupNode`
            GroupNode object or any class that inherits from GroupNode class.

        """
        return self.root.add_group(name=name, geometry=geometry, parent=parent)

    def add_element(self, name=None, element=None, parent=None):
        """Add an :class:`compas_model.model.ElementNode` to the tree.

        Parameters
        ----------
        name : str, optional
            A name or identifier for the node.
        element : :class:`compas_model.elements.Element`, optional
            Element or any classes that inherits from it.
        parent : :class:`compas_model.model.GroupNode`, optional
            The parent node of this node.

        Returns
        -------
        :class:`compas_model.model.ElementNode`
            ElementNode object or any class that inherits from ElementNode class.

        """
        return self.root.add_element(name=name, element=element, parent=parent)
