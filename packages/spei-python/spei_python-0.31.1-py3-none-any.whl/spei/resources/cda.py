from lxml import etree
from pydantic import BaseModel

from spei import types
from spei.utils import to_snake_case, to_upper_camel_case  # noqa: WPS347

SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
PRAXIS_NS = 'http://www.praxis.com.mx/'


class CDA(BaseModel):
    id: int
    mensaje_id: int
    op_fecha_oper: int
    op_hora_abono: int
    op_cve_rastreo: str

    op_clave_emisor: str
    op_nombre_emisor: str

    op_nom_ord: str
    op_tp_cta_ord: types.TipoCuentaOrdenPago
    op_cuenta_ord: str
    op_rfc_curp_ord: str

    op_nombre_receptor: str

    op_nom_ben: str
    op_tp_cta_ben: types.TipoCuentaOrdenPago
    op_cuenta_ben: str
    op_rfc_curp_ben: str

    op_tipo_pag: str
    op_concepto_pag: str

    op_iva: str = None
    op_monto: str = None
    op_hora_00: str = None
    op_fecha_abono: str = None

    op_folio_orig_odp: int = None
    op_folio_orig_paq: int = None

    class Config:  # noqa: WPS306, WPS431
        use_enum_values = True

    def build_xml(self):
        mensaje = etree.Element(
            'datosCda',
            idCda=str(self.id),
            idMensaje=str(self.mensaje_id),
        )

        elements = self.dict(exclude={'id', 'mensaje_id'})

        for element, value in elements.items():  # noqa: WPS110
            if element in self.__fields__:
                upper_camel_case_element = to_upper_camel_case(element)
                subelement = etree.SubElement(mensaje, upper_camel_case_element)
                subelement.text = str(value)

        return mensaje

    @classmethod
    def parse_xml(cls, mensaje_element):
        genera_cda = mensaje_element.find('generaCda')
        datos_cta = genera_cda.find('datosCda')

        cda_data = {
            'id': datos_cta.attrib['idCda'],
            'mensaje_id': datos_cta.attrib['idMensaje'],
        }

        for element in datos_cta.getchildren():
            tag = to_snake_case(element.tag)
            if tag in cls.__fields__:
                cda_data[tag] = element.text

        return cls(**cda_data)
