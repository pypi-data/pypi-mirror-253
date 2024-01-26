from lxml import etree

from spei.resources import Acuse


class XMLElement(object):
    def __new__(cls, respuesta):
        xml_element = respuesta.find(
            'xml',
        )

        return etree.fromstring(xml_element.text)  # noqa: S320


class RespuestaElement(object):
    def __new__(cls, body):
        return body.find(
            '{http://cep.fyg.com/}respuestaCDA',
        )


class BodyElement(object):
    def __new__(cls, mensaje):
        return mensaje.find(
            '{http://schemas.xmlsoap.org/soap/envelope/}Body',
        )


class AcuseResponse(object):
    def __new__(cls, acuse, acuse_cls=Acuse):
        mensaje = etree.fromstring(acuse)  # noqa: S320
        mensaje_element = XMLElement(RespuestaElement(BodyElement((mensaje))))
        return acuse_cls.parse_xml(mensaje_element)
