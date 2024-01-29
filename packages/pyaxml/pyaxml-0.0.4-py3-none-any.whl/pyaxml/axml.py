import sys
try:
    from .proto import axml_pb2
except ImportError:
    print("proto is not build")
    sys.exit(1)
from struct import pack, unpack
from androguard.core.resources import public
import re
import ctypes
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

AXML_HEADER_SIZE=8
AXML_STRING_POOL_HEADER_SIZE=28



class AXMLHeader:
    """AXMLHeader class to build an AXMLHeader
    """

    def __init__(self, type : int = 0, size : int = 0, proto : axml_pb2.AXMLHeader = None):
        """Initialize an AXMLHeader

        Args:
            type (int, optional): type element from ResType. Defaults to 0.
            size (int, optional): size of data contain belong to this AXMLHeader. Defaults to 0.
            proto (axml_pb2.AXMLHeader, optional): define AXMLHeader by a protobuff. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.AXMLHeader()
            self.proto.type = type
            self.proto.size = size
            self.proto.header_size = AXML_HEADER_SIZE
        else:
            self.proto = proto
        

    def pack(self) -> bytes:
        """pack the AXMLHeader element

        Returns:
            bytes: return the AXMLHeader element packed
        """
        return pack("<HHL", self.proto.type, self.proto.header_size, self.proto.size)
    

class AXMLHeader_XML(AXMLHeader):
    """AXMLHeader_XML class to build an AXMLHeader with the type RES_XML_TYPE
    """

    def __init__(self, size : int = 0, proto : axml_pb2.AXMLHeader = None):
        """Initialize an AXMLHeader with the type RES_XML_TYPE

        Args:
            size (int, optional): size of data contain belong to this AXMLHeader. Defaults to 0.
            proto (axml_pb2.AXMLHeader, optional): define AXMLHeader by a protobuff. Defaults to None.
        """
        if proto is None:
            super().__init__(axml_pb2.RES_XML_TYPE, size)
        else:
            self.proto = proto


class AXMLHeader_STRING_POOL:
    """AXMLHeader_STRING_POOL class to build an AXMLHeader_STRING_POOL element
    """

    def __init__(self, sb : list = None, size : int = 0, proto : axml_pb2.AXMLHeader_STRING_POOL = None):
        """Initialize an AXMLHeader of STRING_POOL

        Args:
            sb (list, optional): list of Stringblock elements. Defaults to None.
            size (int, optional): size of data contain belong to this AXMLHeader. Defaults to 0.
            proto (axml_pb2.AXMLHeader_STRING_POOL, optional): define AXMLHeader_STRING_POOL by a protobuff. Defaults to None.
        """
        # TODO make version with initilisation without proto
        if proto:
            self.proto = proto
    
    def compute(self):
        """Compute all fields to have a Stringpool element
        """
        pass

    def pack(self) -> bytes:
        """pack the AXMLHeader_STRING_POOL element

        Returns:
            bytes: return the AXMLHeader_STRING_POOL element packed
        """
        return AXMLHeader(proto=self.proto.hnd).pack() + pack("<LLLLL", self.proto.len_stringblocks, self.proto.len_styleblocks,
                                                                        self.proto.flag, self.proto.stringoffset, self.proto.styleoffset)


##############################################################################
#
#                              STRINGBLOCKS
#
##############################################################################


class StringBlock:
    """StringBlock class to build an StringBlock element
    """

    def __init__(self, data : str = "", size : int = 0, utf8 : bool = False, proto : axml_pb2.StringBlock = None):
        """initialize a stringblock element

        Args:
            data (str, optional): value of the stringblock. Defaults to "".
            size (int, optional): size of data contain belong to this Stringblock. Defaults to 0.
            utf8 (bool, optional): Stringblock can be encoded in UTF8 or UTF16. set True if you want to encode in UTF8 else UTF16. Defaults to False.
            proto (axml_pb2.StringBlock, optional): define StringBlock by a protobuff. Defaults to None.
        """
        if proto:
            self.proto = proto
            self.utf8= utf8
        else:
            self.proto = axml_pb2.StringBlock()
            self.proto.data = data
            self.proto.size = size
            self.utf8= utf8
    
    def compute(self):
        """Compute all fields to have a StringBlock element
        """
        self.proto.size = len(self.proto.data)
    
    def pack(self) -> bytes:
        """pack the StringBlock element

        Returns:
            bytes: return the StringBlock element packed
        """
        if self.utf8:
            return pack('<BB', self.proto.size, self.proto.size) + self.proto.data.encode('utf-8')[2:] + b'\x00'
        else:
            return pack("<H", self.proto.size) + self.proto.data.encode('utf-16')[2:] + b'\x00\x00'

class StringBlocks:
    """StringBlocks class to build all StringBlocks elements
    """
 
    def __init__(self, proto : axml_pb2.StringBlocks = None):
        """initialize the bunch of StringBlocks element

        Args:
            proto (axml_pb2.StringBlocks, optional): define Stringblocks by a protobuff. Defaults to None.
        """
        if proto:
            self.proto = proto
        else:
            self.proto = axml_pb2.StringBlocks()
    
    def compute(self):
        """Compute all fields to have all StringBlocks elements
        """

        idx = 0
        for s in self.proto.stringblocks:
            self.proto.stringoffsets.append(idx)
            idx += len(StringBlock(proto=s, utf8=self.proto.hnd.flag & axml_pb2.UTF8_FLAG == axml_pb2.UTF8_FLAG).pack())

        self.proto.hnd.stringoffset = AXML_STRING_POOL_HEADER_SIZE + \
            len(b"".join(pack('<I', x) for x in self.proto.stringoffsets)) + \
            len(b"".join(pack('<I', x) for x in self.proto.styleoffsets))
        
        self.proto.hnd.styleoffset = 0

        self.proto.hnd.hnd.CopyFrom(AXMLHeader(axml_pb2.RES_STRING_POOL_TYPE, len(self.pack())).proto)
        self.proto.hnd.hnd.header_size = AXML_STRING_POOL_HEADER_SIZE
        self.proto.hnd.len_stringblocks = len(self.proto.stringoffsets)
        self.proto.hnd.len_styleblocks = len(self.proto.styleoffsets)

    def pack(self) -> bytes:
        """pack the StringBlocks element

        Returns:
            bytes: return the StringBlocks element packed
        """
        sb_offsets = b"".join(pack('<I', x) for x in self.proto.stringoffsets)
        st_offsets = b"".join(pack('<I', x) for x in self.proto.styleoffsets)
        sb = self.align(b"".join(StringBlock(proto=elt, utf8=self.proto.hnd.flag & axml_pb2.UTF8_FLAG == axml_pb2.UTF8_FLAG).pack() for elt in self.proto.stringblocks))
        st = b"" # TODO
        return AXMLHeader_STRING_POOL(proto=self.proto.hnd).pack() + sb_offsets + st_offsets + sb + st
    
    def align(self, buf : bytes) -> bytes:
        """Align stringblocks elements

        Args:
            buf (bytes): align the buffer given in input

        Returns:
            bytes: return the element with padding to align
        """
        return buf + b"\x00" * (4 - (len(buf) % 4))

    def get(self, name : str) -> int:
        """Get index of a stringblock or if it doesn't exist append a new one.

        Args:
            name (str): the name of the stringblock

        Returns:
            int: return the index of the stringblock
        """
        try:
            index = self.index(name)
        except ValueError:
            index = len(self.proto.stringblocks)
            tmp = StringBlock(data=name, utf8=self.proto.hnd.flag & axml_pb2.UTF8_FLAG == axml_pb2.UTF8_FLAG)
            tmp.compute()
            self.proto.stringblocks.append(tmp.proto)
        return index
    
    def index(self, name : str) -> int:
        """Get index of a stringblock or if it doesn't exist raise an error

        Args:
            name (str): the name of the stringblock
        
        Raises:
            ValueError: raise ValueError if this element didn't exist

        Returns:
            int: return the index of the stringblock
        """
        for i in range(0, len(self.proto.stringblocks)):
            if self.proto.stringblocks[i].data == name:
                return i
        raise ValueError

##############################################################################
#
#                              RESOURCEMAP
#
##############################################################################

class ResourceMap:
    """ResourceMap class to build all ResourceMap elements
    """


    def __init__(self, res : [StringBlock] = [], proto : axml_pb2.ResourceMap = None):
        """initialize ResourceMap element

        Args:
            res (StringBlock], optional): List of StringBlock elements. Defaults to [].
            proto (axml_pb2.ResourceMap, optional): define ResourceMap by a protobuff. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.ResourceMap()
            self.proto.res.extend(res)
            self.proto.header.CopyFrom(AXMLHeader(axml_pb2.RES_XML_RESOURCE_MAP_TYPE, 8).proto)
            self.proto.header.size = AXML_HEADER_SIZE + 4 * len(res)
        else:
            self.proto = proto
    
    def pack(self) -> bytes:
        """pack the ResourceMap element

        Returns:
            bytes: return the ResourceMap element packed
        """
        return AXMLHeader(proto=self.proto.header).pack() + b"".join(pack("<L", x) for x in self.proto.res)

##############################################################################
#
#                              XML ELEMENTS
#
##############################################################################

class AXMLHeader_RES_XML(AXMLHeader):
    """AXMLHeader_RES_XML class to build an header of RES_XML
    """

    def __init__(self, type=0, size=0, proto : axml_pb2.AXMLHeader = None):
        """Initialize header of Res_XML

        Args:
            type (int, optional): define the type. Defaults to 0.
            size (int, optional): define the size of whole element. Defaults to 0.
            proto (axml_pb2.AXMLHeader, optional): define RES_XML header by a protobuff. Defaults to None.
        """
        if proto is None:
            super().__init__(type, size + 8, proto)
            self.proto.header_size = 16
        else:
            self.proto = proto 

class AXMLHeader_START_ELEMENT(AXMLHeader_RES_XML):
    """AXMLHeader_START_ELEMENT class to build an header of Start element
    """

    def __init__(self, size : int):
        """initialize START_ELEMENT element

        Args:
            size (int): size of START_ELEMENT and its header
        """
        super().__init__(axml_pb2.RES_XML_START_ELEMENT_TYPE, size)

class AXMLHeader_END_ELEMENT(AXMLHeader_RES_XML):
    """AXMLHeader_END_ELEMENT class to build an header of End element
    """

    def __init__(self, size : int):
        """initialize END_ELEMENT element

        Args:
            size (int): size of END_ELEMENT and its header
        """
        super().__init__(axml_pb2.RES_XML_END_ELEMENT_TYPE, size)

class AXMLHeader_START_NAMESPACE(AXMLHeader_RES_XML):
    """AXMLHeader_START_NAMESPACE class to build an header of Start namespace
    """

    def __init__(self, size : int):
        """initialize START_NAMESPACE element

        Args:
            size (int): size of START_NAMESPACE and its header
        """
        super().__init__(axml_pb2.RES_XML_START_NAMESPACE_TYPE, size)

class AXMLHeader_END_NAMESPACE(AXMLHeader_RES_XML):
    """AXMLHeader_END_NAMESPACE class to build an header of End namespace
    """

    def __init__(self, size : int):
        """initialize END_NAMESPACE element

        Args:
            size (int): size of END_NAMESPACE and its header
        """
        super().__init__(axml_pb2.RES_XML_END_NAMESPACE_TYPE, size)

class Classical_RES_XML:
    """RES_XML class to build RES_XML element
    """

    def __init__(self, lineNumber : int = 0, Comment : int = 0xffffffff, proto : axml_pb2.ResXML = None):
        """initialize RES_XML element

        Args:
            lineNumber (int, optional): _description_. Defaults to 0.
            Comment (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.ResXML, optional): define RES_XML by a protobuff. Defaults to None.
        """
        if proto is None:
            self.proto.generic.lineNumber = lineNumber
            self.proto.generic.Comment = Comment
        else:
            self.proto.generic.CopyFrom(proto)

    @property
    def content(self):
        return pack('<LL', self.proto.generic.lineNumber, self.proto.generic.Comment)
    
    def compute(self):
        """Compute all fields to have all RES_XML elements
        """
        pass

    def pack(self) -> bytes:
        """pack the RES_XML element

        Returns:
            bytes: return the RES_XML element packed
        """
        return self.content

class RES_XML_START_ELEMENT(Classical_RES_XML):

    def __init__(self, namespaceURI : int = 0xffffffff, name : int =0xffffffff, attributes : list = [],
            styleAttribute : int = -1, classAttribute : int = -1, lineNumber : int = 0, Comment : int = 0xffffffff,
            proto : axml_pb2.ResXMLStartElement = None):
        """_summary_

        Args:
            namespaceURI (int, optional): _description_. Defaults to 0xffffffff.
            name (int, optional): _description_. Defaults to 0xffffffff.
            attributes (list, optional): _description_. Defaults to [].
            styleAttribute (int, optional): _description_. Defaults to -1.
            classAttribute (int, optional): _description_. Defaults to -1.
            lineNumber (int, optional): _description_. Defaults to 0.
            Comment (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.ResXMLStartElement, optional): _description_. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.ResXMLStartElement()
            super().__init__(lineNumber, Comment)
            self.proto.namespaceURI = namespaceURI
            self.proto.name = name
            self.proto.attributes.extend(attributes)
            self.proto.styleAttribute = styleAttribute
            self.proto.classAttribute = classAttribute
        else:
            self.proto = proto
            super().__init__(proto=proto.generic)
            

    def compute(self):
        """Compute all fields to have all RES_XML_START_ELEMENT elements
        """
        self.proto.len_attributes = len(self.proto.attributes)
        super().compute()

    @property
    def content(self) -> bytes:
        """_summary_

        Returns:
            bytes: _description_
        """
        return super().content + pack('<LLLLhh',
                self.proto.namespaceURI,
                self.proto.name,
                0x140014, # potential attribute value
                self.proto.len_attributes,
                self.proto.styleAttribute,
                self.proto.classAttribute) + \
                        b"".join(Attribute(proto=a).pack() for a in self.proto.attributes)

class RES_XML_END_ELEMENT(Classical_RES_XML):

    def __init__(self, namespaceURI : int = 0xffffffff, name : int = 0xffffffff,
                 lineNumber : int = 0, Comment : int = 0xffffffff,
                 proto : axml_pb2.ResXMLEndElement = None):
        """_summary_

        Args:
            namespaceURI (int, optional): _description_. Defaults to 0xffffffff.
            name (int, optional): _description_. Defaults to 0xffffffff.
            lineNumber (int, optional): _description_. Defaults to 0.
            Comment (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.ResXMLEndElement, optional): _description_. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.ResXMLEndElement()
            super().__init__(lineNumber, Comment)
            self.proto.namespaceURI = namespaceURI
            self.proto.name = name
        else:
            self.proto = proto
            super().__init__(proto=proto.generic)
            


    @property
    def content(self) -> bytes:
        """_summary_

        Returns:
            bytes: _description_
        """
        return super().content + pack('<LL',
                self.proto.namespaceURI,
                self.proto.name)

class RES_XML_START_NAMESPACE(Classical_RES_XML):

    def __init__(self, prefix : int = 0xffffffff, uri : int = 0xffffffff,
                lineNumber : int = 0, Comment : int = 0xffffffff,
                proto : axml_pb2.ResXMLStartNamespace = None):
        """_summary_

        Args:
            prefix (int, optional): _description_. Defaults to 0xffffffff.
            uri (int, optional): _description_. Defaults to 0xffffffff.
            lineNumber (int, optional): _description_. Defaults to 0.
            Comment (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.ResXMLStartNamespace, optional): _description_. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.ResXMLStartNamespace()
            super().__init__(lineNumber, Comment)
            self.proto.prefix = prefix
            self.proto.uri = uri
        else:
            self.proto = proto
            super().__init__(proto=proto.generic)
            

    @property
    def content(self) -> bytes:
        """_summary_

        Returns:
            bytes: _description_
        """
        return super().content + pack('<LL',
                self.proto.prefix,
                self.proto.uri)

class RES_XML_END_NAMESPACE(Classical_RES_XML):

    def __init__(self, prefix : int = 0xffffffff, uri : int = 0xffffffff,
                 lineNumber : int = 0, Comment : int = 0xffffffff,
                 proto : axml_pb2.ResXMLEndNamespace = None):
        """_summary_

        Args:
            prefix (int, optional): _description_. Defaults to 0xffffffff.
            uri (int, optional): _description_. Defaults to 0xffffffff.
            lineNumber (int, optional): _description_. Defaults to 0.
            Comment (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.ResXMLEndNamespace, optional): _description_. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.ResXMLEndNamespace()
            super().__init__(lineNumber, Comment)
            self.proto.prefix = prefix
            self.proto.uri = uri
        else:
            self.proto = proto
            super().__init__(proto=proto.generic)
            

    @property
    def content(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return super().content + pack('<LL',
                self.proto.prefix,
                self.proto.uri)
    

class Attribute:

    def __init__(self, namespaceURI : int = 0xffffffff, name : int = 0xffffffff, value : int = 0xffffffff, type : int = 0xffffffff, data : int = 0xffffffff, proto : axml_pb2.Attribute = None):
        """_summary_

        Args:
            namespaceURI (int, optional): _description_. Defaults to 0xffffffff.
            name (int, optional): _description_. Defaults to 0xffffffff.
            value (int, optional): _description_. Defaults to 0xffffffff.
            type (int, optional): _description_. Defaults to 0xffffffff.
            data (int, optional): _description_. Defaults to 0xffffffff.
            proto (axml_pb2.Attribute, optional): _description_. Defaults to None.
        """
        if proto is None:
            self.proto = axml_pb2.Attribute()
            self.proto.namespaceURI = namespaceURI
            self.proto.name = name
            self.proto.value = value
            self.proto.type = type
            self.proto.data = data
        else:
            self.proto = proto

    def pack(self) -> bytes:
        """pack the Attribute element

        Returns:
            bytes: return the Attribute element packed
        """
        return pack('<LLLLL', self.proto.namespaceURI, self.proto.name, self.proto.value,
                self.proto.type, self.proto.data)



class RessourceXML:

    def __init__(self, proto : axml_pb2.RessourceXML = None) -> None:
        """_summary_

        Args:
            proto (axml_pb2.RessourceXML, optional): _description_. Defaults to None.
        """
        if proto:
            self.proto = proto
        else:
            self.proto = axml_pb2.RessourceXML()
    
    def pack(self) -> bytes:
        """pack the RessourceXML element

        Returns:
            bytes: return the RessourceXML element packed
        """
        buf = b""
        for elt in self.proto.elts:
            header = AXMLHeader(proto=elt.header).pack()
            if elt.HasField('start_elt'):
                buf += header + RES_XML_START_ELEMENT(proto=elt.start_elt).pack()
            elif elt.HasField('end_elt'):
                buf += header + RES_XML_END_ELEMENT(proto=elt.end_elt).pack()
            elif elt.HasField('start_ns'):
                buf += header + RES_XML_START_NAMESPACE(proto=elt.start_ns).pack()
            elif elt.HasField('end_ns'):
                buf += header + RES_XML_END_NAMESPACE(proto=elt.end_ns).pack()
        return buf


##############################################################################
#
#                              AXML OBJECT
#
##############################################################################


class AXML:

    def __init__(self, proto : axml_pb2.AXML = None):
        """_summary_

        Args:
            proto (axml_pb2.AXML, optional): _description_. Defaults to None.
        """
        if proto:
            self.proto = proto
            self.stringblocks = StringBlocks(proto=self.proto.stringblocks)
        else:
            self.proto = axml_pb2.AXML()
            self.stringblocks = StringBlocks()
    
    @property
    def get_proto(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self.proto.stringblocks = self.stringblocks.proto
        return self.proto

    ###########################################
    #                                         #
    #           ENOCDE from XML               #
    #                                         #
    ###########################################
    
    def from_xml(self, root : etree.ElementBase):
        """Convert Xml to Axml object

        Args:
            root (etree.ElementBase): Xml representation of AXML object
        """
        self.add_all_attrib(root)
        self.start_namespace("http://schemas.android.com/apk/res/android", "android")
        self.__from_xml_etree(root)
        self.end_namespace("http://schemas.android.com/apk/res/android", "android")
        self.compute()
   
    
    def __from_xml_etree(self, root : etree.ElementBase):
        """Convert Xml to Axml object internally

        Args:
            root (etree.ElementBase): Xml representation of AXML object
        """
        self.start(root.tag, root.attrib)
        for e in root:
            self.__from_xml_etree(e)
        self.end(root.tag)

    
    def add_xml_elt(self, res_xml : Classical_RES_XML, header_xml : AXMLHeader_RES_XML):
        """Function to add an element in function of the type

        Args:
            res_xml (Classical_RES_XML): Element
            header_xml (AXMLHeader_RES_XML): Header
        """
        res_xml.compute()

        header = header_xml(len(res_xml.content))

        elt = axml_pb2.XMLElement()
        elt.header.CopyFrom(header.proto)
        if type(res_xml.proto) is axml_pb2.ResXMLStartElement:
            elt.start_elt.CopyFrom(res_xml.proto)
        elif type(res_xml.proto) is axml_pb2.ResXMLStartNamespace:
            elt.start_ns.CopyFrom(res_xml.proto)
        elif type(res_xml.proto) is axml_pb2.ResXMLEndNamespace:
            elt.end_ns.CopyFrom(res_xml.proto)
        elif type(res_xml.proto) is axml_pb2.ResXMLEndElement:
            elt.end_elt.CopyFrom(res_xml.proto)
        self.proto.resourcexml.elts.append(elt)

    def start(self, root : str, attrib : dict):
        """Create start of element

        Args:
            root (str): Name of element
            attrib (dict): dict of all attribute of this element
        """
        index = self.stringblocks.get(root)
        i_namespace = self.stringblocks.get("android")
        attributes = []

        dic_attrib = attrib.items()
        for k, v in dic_attrib:
            tmp = k.split('{')
            if len(tmp) > 1:
                tmp = tmp[1].split('}')
                name = self.stringblocks.get(tmp[1])
                namespace = self.stringblocks.get(tmp[0])
            else:
                namespace = 0xffffffff
                name = self.stringblocks.get(k)

            if v == "true":
                attributes.append(Attribute(namespace, name, 0xffffffff, 0x12000000, 1).proto)
            elif v == "false":
                attributes.append(Attribute(namespace, name, 0xffffffff, 0x12000000, 0).proto)
            elif re.search("^@android:[0-9a-fA-F]+$", v):
                attributes.append(Attribute(namespace, name, 0xffffffff, 0x1000000, int(v[-8:], 16)).proto)
            elif re.search("^@[0-9a-fA-F]+$", v):
                attributes.append(Attribute(namespace, name, 0xffffffff, 0x1000000, int(v[1:], 16)).proto)
            elif re.search("^0x[0-9a-fA-F]+$", v):
                attributes.append(Attribute(namespace, name, 0xffffffff, 0x11000000, int(v[2:], 16)).proto)
            else:
                if self.stringblocks.proto.stringblocks[name].data == "versionName":
                    value = self.stringblocks.get(v)
                    attributes.append(Attribute(namespace, name, value, 0x3000008, value).proto)
                elif self.stringblocks.proto.stringblocks[name].data == "compileSdkVersionCodename":
                    value = self.stringblocks.get(v)
                    attributes.append(Attribute(namespace, name, value, 0x3000008, value).proto)
                else:
                    try:
                        value = ctypes.c_uint32(int(v)).value
                        attributes.append(Attribute(namespace, name, 0xffffffff, 0x10000008, value).proto)
                    except ValueError:
                        try:
                            value = unpack('>L', pack('!f', float(v)))[0]
                            attributes.append(Attribute(namespace, name, 0xffffffff, 0x04000008, value).proto)
                        except ValueError:
                            value = self.stringblocks.get(v)
                            attributes.append(Attribute(namespace, name, value, 0x3000008, value).proto)


        content = RES_XML_START_ELEMENT(0xffffffff, index, attributes)
        self.add_xml_elt(content, AXMLHeader_START_ELEMENT)


    def start_namespace(self, prefix : str, uri : str):
        """Create start of namespace

        Args:
            prefix (str): prefix of namespace
            uri (str): uri of namespace
        """
        index = self.stringblocks.get(prefix)
        i_namespace = self.stringblocks.get(uri)


        content = RES_XML_START_NAMESPACE(i_namespace, index)
        self.add_xml_elt(content, AXMLHeader_START_NAMESPACE)

    def end_namespace(self, prefix : str, uri : str):
        """Create end of namespace

        Args:
            prefix (str): prefix of namespace
            uri (str): uri of namespace
        """
        index = self.stringblocks.get(prefix)
        i_namespace = self.stringblocks.get(uri)


        content = RES_XML_END_NAMESPACE(i_namespace, index)
        self.add_xml_elt(content, AXMLHeader_END_NAMESPACE)

    def end(self, attrib : str):
        """Create end of element

        Args:
            attrib (str): name of end element
        """
        index = self.stringblocks.index(attrib)
        i_namespace = self.stringblocks.index("android")

        content = RES_XML_END_ELEMENT(0xffffffff, index)
        self.add_xml_elt(content, AXMLHeader_END_ELEMENT)

    def add_all_attrib(self, root : etree.ElementBase):
        """Create Ressource Map

        Args:
            root (etree.ElementBase): XML representation of AXML
        """
        res = []
        namespace = "{http://schemas.android.com/apk/res/android}"
        queue = [root]
        while len(queue) > 0:
            r = queue.pop()
            for child in r:
                queue.append(child)
            for k in r.attrib.keys():
                if k.startswith(namespace):
                    name = k[len(namespace):]
                    if name in public.SYSTEM_RESOURCES['attributes']['forward']:
                        val = public.SYSTEM_RESOURCES['attributes']['forward'][name]
                        if not val in res:
                            self.stringblocks.get(name)
                            res.append(val)
        self.proto.resourcemap.CopyFrom(ResourceMap(res=res).proto)

    ###########################################
    #                                         #
    #           ENOCDE from XML               #
    #                                         #
    ###########################################
    
    def compute(self):
        """Compute all fields to have all AXML elements
        """
        self.stringblocks.compute()
        self.proto.header_xml.CopyFrom(AXMLHeader_XML(len(self.pack())).proto)

    def pack(self) -> bytes:
        """pack the AXML element

        Returns:
            bytes: return the AXML element packed
        """
        self.proto.stringblocks.CopyFrom(self.stringblocks.proto)
        sb_pack = self.stringblocks.pack()
        res = ResourceMap(proto=self.proto.resourcemap).pack()
        resxml = RessourceXML(proto=self.proto.resourcexml).pack()
        header_xml = AXMLHeader_XML(proto=self.proto.header_xml).pack()
        return header_xml + sb_pack + res + resxml

