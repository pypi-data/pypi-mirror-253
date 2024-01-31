import xml.dom
from importlib.metadata import version

from triade.thesaurus import Thesaurus
import triade.errors as err


class TriadeDocument:
    def __init__(self, data):
        self._data = data
        data = Thesaurus(data)
        tag_name = data.get(["tagName", "tag_name"])
        self._node = self._create_document(tag_name)

        self._root = TriadeElement(data, parent=self, document=self)

    def __str__(self):
        return "<?document %s ?>" % (self._node.documentElement.tagName)

    def __repr__(self):
        cls = type(self).__name__
        data = repr(self._data)
        return "%s(%s)" % (cls, data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._node.unlink()
        return False

    @property
    def node(self):
        """The XML DOM Document object associated with this object."""
        return self._node

    @property
    def root(self):
        """The root TriadeElement associated with this document."""
        return self._root

    @property
    def parent(self):
        """None"""
        return None

    def create_element(self, tag_name):
        """Create and return a new instance of XML DOM Element"""
        return self._node.createElement(tag_name)

    def create_attribute(self, name, value):
        """Create and return a new instance of XML DOM Attr"""
        attr = self._node.createAttribute(name)
        attr.value = value
        return attr

    def create_text_node(self, text):
        """Create and return a new instance of XML DOM TextNode"""
        return self._node.createTextNode(text)

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        return self._node.toprettyxml(*args, **kwargs)

    def unlink(self):
        self._node.unlink()

    def _create_document(self, name):
        impl = xml.dom.getDOMImplementation()
        return impl.createDocument(xml.dom.EMPTY_NAMESPACE, name, None)


class TriadeElement:
    def __init__(self, data, *, parent=None, document=None):
        self._validate(data)
        data = Thesaurus(data)
        self._data = data
        self._parent = parent
        self._document = document

        self._tag_name = data.get(["tagName", "tag_name"])

        child_nodes = data.get(["childNodes", "child_nodes"], [])
        if child_nodes is None:
            child_nodes = []

        self._children = TriadeNodeList(child_nodes, parent=self,
                                        document=document)

        if isinstance(parent, TriadeDocument):
            self._node = parent.node.documentElement
        else:
            self._node = document.create_element(self._tag_name)

        for child_node in self._children:
            self._node.appendChild(child_node.node)

        attributes = data.get("attributes", {})
        self._attrs = TriadeNamedNodeMap(attributes, element=self)

    def __str__(self):
        size = len(self)
        if size == 0:
            return "<?element %s ?>" % (self.tag_name)
        return '<?element %s childNodes="%d" ?>' % (self.tag_name, size)

    def __repr__(self):
        cls = type(self).__name__
        data = dict(self._data)
        return "%s(%s)" % (cls, repr(data))

    def __len__(self):
        try:
            return len(self._children)
        except AttributeError:
            return 0

    def __iter__(self):
        return iter(self._children)

    def __getitem__(self, key):
        if key in ["tagName", "tag_name"]:
            return self._tag_name
        elif key in ["childNodes", "child_nodes"]:
            return self._children
        elif key == "attributes":
            return self._attrs
        elif isinstance(key, str):
            raise KeyError('"%s" key is not present in objects of type %s.' %
                           (key, type(self).__name__))
        else:
            return self._children[key]

    def __setitem__(self, key, value):
        if key in ["tagName", "tag_name"]:
            msg = "Tag name reassignment is not allowed"
            raise err.TriadeForbiddenWriteError(msg)

    def __delitem__(self, key):
        pass

    @property
    def node(self):
        """The XML DOM Element object associated with this object."""
        return self._node

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._document

    @property
    def tagName(self):
        """The element's tag name."""
        return self._tag_name

    @tagName.setter
    def tagName(self, value):
        if not isinstance(value, str):
            raise err.TriadeNodeTypeError('"tagName" value must be a string.')
        self._tag_name = value

    @tagName.deleter
    def tagName(self):
        raise err.TriadeXMLException("Deleting tagName is not allowed.")

    tag_name = property(tagName.fget, tagName.fset, tagName.fdel)

    @property
    def childNodes(self):
        """The element's child nodes as a list."""
        return self._children

    @childNodes.setter
    def childNodes(self, _):
        msg = "Reassignment of child nodes list is not allowed."
        raise err.TriadeForbiddenWriteError(msg)

    @childNodes.deleter
    def childNodes(self):
        self._children = []

    child_nodes = property(childNodes.fget, childNodes.fset, childNodes.fdel)

    @property
    def attributes(self):
        """The element's attributes as a dictionary."""
        return self._attrs

    @attributes.setter
    def attributes(self, _):
        msg = "Reassignment of attributes list is not allowed"
        raise err.TriadeForbiddenWriteError(msg)

    @attributes.deleter
    def attributes(self):
        self._attrs = {}

    def append(self, obj, /):
        self._children.append(obj)

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        return self._node.toprettyxml(*args, **kwargs)

    def _validate(self, data):
        if not isinstance(data, dict):
            raise err.TriadeNodeTypeError('"data" should be a dictionary.')

        if ["tagName", "tag_name"] not in Thesaurus(data):
            raise err.TriadeNodeValueError('"tagName" not found in "data".')


class TriadeNodeList:
    def __init__(self, data, *, parent=None, document=None):
        self._validate(data)

        self._parent = parent
        self._document = document

        self._nodes = []
        for elem in data:
            if elem is None:
                continue
            if isinstance(elem, dict):
                child_node = TriadeElement(elem, parent=parent, document=document)
            elif isinstance(elem, (str, int, float)):
                child_node = TriadeTextNode(str(elem), parent=parent,
                                            document=document)

            self._nodes.append(child_node)

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, index):
        return self._nodes[index]

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._document

    def append(self, obj, /):
        if not isinstance(obj, (dict, str)):
            msg = "The appended value should be a dict or str."
            raise err.TriadeNodeTypeError(msg)

        if isinstance(obj, dict):
            node = TriadeElement(obj, parent=self.parent, document=self.document)
        elif isinstance(obj, str):
            node = TriadeTextNode(obj, parent=self.parent, document=self.document)

        self._nodes.append(node)
        self.parent.node.appendChild(node.node)

    def _validate(self, data):
        if not isinstance(data, list):
            raise err.TriadeNodeTypeError('"data" should be a list.')

        for node in data:
            if node is None:
                continue
            if not isinstance(node, (dict, str, int, float)):
                msg = 'Every value in "data" should be a dict, str, int or float.'
                raise err.TriadeNodeValueError(msg)


class TriadeAttribute:
    def __init__(self, name, value, *, element=None):
        if name.count(":") > 1:
            msg = "Attribute name should contain at most one colon."
            raise err.TriadeNodeValueError(msg)

        self._element = element
        self._node = self._element.document.create_attribute(name, value)
        self.element.node.setAttribute(name, value)

    def __str__(self):
        return '<?attr %s="%s" ?>' % (self._node.name, self._node.value)

    def __repr__(self):
        cls = type(self).__name__
        return "%s(%s, %s)" % (cls, repr(self._node.name), repr(self._node.value))

    def __getitem__(self, key):
        if key not in ["name", "value"]:
            msg = "The key %s is not present in TriadeAttribute." % (key,)
            raise err.TriadeNodeKeyError(msg)

        if key == "name":
            return self._node.name
        elif key == "value":
            return self._node.value

    def __setitem__(self, key, value):
        if key not in ["name", "value"]:
            msg = 'The only keys allowed for TriadeAttribute are "name" and "value".'
            raise err.TriadeNodeKeyError(msg)

        if key == "name":
            self._node.name = value
        elif key == "value":
            self._node.value = value

    def __delitem__(self, key):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def element(self):
        return self._element

    @property
    def document(self):
        return self._element.document

    @property
    def node(self):
        return self._node

    @property
    def name(self):
        """The attribute's name."""
        return self._node.name

    @name.setter
    def name(self, new_name):
        self._node.name = new_name

    @name.deleter
    def name(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def value(self):
        """The attribute's value."""
        return self._node.value

    @value.setter
    def value(self, new_value):
        self._node.value = new_value

    @value.deleter
    def value(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def node(self):
        """The XML DOM Attr object associated with this object."""
        return self._node

    @property
    def localName(self):
        parts = self.name.split(":")
        return parts[1] if len(parts) > 1 else self.name

    @property
    def prefix(self):
        parts = self.name.split(":")
        return parts[0] if len(parts) > 1 else ""

    @property
    def namespaceURI(self):
        return self._node.namespaceURI

    nodeName = property(name.fget, name.fset, name.fdel)
    nodeValue = property(value.fget, value.fset, value.fdel)


class TriadeNamedNodeMap:
    def __init__(self, attributes, *, element=None):
        self._attrs = {}
        self._len = 0
        self._element = element

        if attributes is None:
            attributes = {}

        self._validate(attributes)

        for name, value in attributes.items():
            self._attrs[name] = TriadeAttribute(name, str(value),
                                                element=element)
            self._len += 1

    def __str__(self):
        values = self._attrs.values()

        if len(values) == 0:
            return "<?attributeList ?>"

        text = " ".join('%s="%s"' % (attr.name, attr.value) for attr in values)
        return "<?attributeList %s ?>" % (text)

    def __repr__(self):
        cls = type(self).__name__
        text = ", ".join("%s: %s" % (repr(attr.name), repr(attr.value))
                         for attr in self._attrs.values())

        if self._element is not None:
            return "%s({%s}, %s)" % (cls, text, repr(self._element))

        return "%s({%s})" % (cls, text)

    def __iter__(self):
        return iter(self._attrs.values())

    def __contains__(self, name):
        return name in self._attrs

    def __getitem__(self, name):
        return self._attrs[name]

    def __setitem__(self, name, value):
        if name in self._attrs:
            self._change_value(name, value)
        else:
            self._add_value(name, value)

    def __delitem__(self, name):
        del self._attrs[name]
        self._len -= 1

    def __len__(self):
        return self._len

    def get(self, name, default=None):
        return self._attrs.get(name, default)

    def item(self, index):
        try:
            return list(self._attrs.values())[index]
        except IndexError:
            return None

    def items(self):
        return [(a.name, a.value) for a in self._attrs.values()]

    def keys(self):
        return self._attrs.keys()

    def values(self):
        return self._attrs.values()

    def _add_value(self, name, value):
        if isinstance(value, (list, tuple)):
            new_name  = value[0]
            new_value = value[1]
        elif isinstance(value, dict):
            new_name  = value["name"]
            new_value = value["value"]
        elif isinstance(value, str):
            new_name  = name
            new_value = value
        else:
            msg = ("You can't assign a value of type %s to the \"%s\" attribute" %
                   (type(value).__name__, name))
            raise err.TriadeNodeTypeError(msg)

        self._attrs[name] = TriadeAttribute(new_name, new_value)
        self._len += 1

    def _change_value(self, name, value):
        if isinstance(value, (list, tuple)):
            new_name  = value[0]
            new_value = value[1]

            self._attrs[name].name  = new_name
            self._attrs[name].value = new_value

            self._attrs[new_name] = self._attrs[name]
            del self._attrs[name]
        elif isinstance(value, dict):
            new_name  = value["name"]
            new_value = value["value"]

            self._attrs[name].name  = new_name
            self._attrs[name].value = new_value

            self._attrs[new_name] = self._attrs[name]
            del self._attrs[name]
        elif isinstance(value, str):
            self._attrs[name].value = value
        else:
            msg = ("You can't assign a value of type %s to the \"%s\" key." %
                   (type(value).__name__, name))
            raise err.TriadeNodeTypeError(msg)

    def _validate(self, attributes):
        if not isinstance(attributes, dict):
            msg = "Input for TriadeNamedNodeMap should be a dictionary."
            raise TriadeNodeTypeError(msg)


class TriadeTextNode:
    def __init__(self, data, *, parent=None, document=None):
        self._parent = parent
        self._document = document
        self._node = self._document.create_text_node(data)

    def __str__(self):
        return self._node.data

    def __repr__(self):
        cls = type(self).__name__
        return "%s(%s)" % (cls, repr(self._node.data))

    @property
    def node(self):
        """The XML DOM TextNode object associated with this object."""
        return self._node

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._document

    @property
    def data(self):
        """The content of the text node as a string."""
        return self._node.data

    @data.setter
    def data(self, value):
        self._node.data = value

    @data.deleter
    def data(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        return self._node.toprettyxml(*args, **kwargs)
