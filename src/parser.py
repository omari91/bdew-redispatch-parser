import pandas as pd
from lxml import etree
from typing import Optional
import os

class BDEWParser:
    """
    Parses and validates BDEW-style XML files for Redispatch processes.
    """

    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self._xsd_schema = self._load_schema()

    def _load_schema(self) -> Optional[etree.XMLSchema]:
        """Loads and compiles the XSD schema."""
        if not os.path.exists(self.schema_path):
            raise FileNotFoundError(f"Schema not found at {self.schema_path}")

        try:
            xml_schema_doc = etree.parse(self.schema_path)
            return etree.XMLSchema(xml_schema_doc)
        except etree.XMLSchemaParseError as e:
            print(f"Schema Parse Error: {e}")
            raise

    def validate(self, xml_path: str) -> bool:
        """Validates an XML file against the loaded XSD schema."""
        if not os.path.exists(xml_path):
            raise FileNotFoundError(f"XML file not found at {xml_path}")

        try:
            xml_doc = etree.parse(xml_path)
            self._xsd_schema.assertValid(xml_doc)
            print(f"Validation Successful: {os.path.basename(xml_path)} matches XSD.")
            return True
        except etree.DocumentInvalid as e:
            print(f"Validation Failed: {e}")
            return False

    def parse_to_dataframe(self, xml_path: str) -> pd.DataFrame:
        """Parses the XML payload into a Pandas DataFrame."""
        tree = etree.parse(xml_path)
        root = tree.getroot()

        data_rows = []

        # Iterate through AvailabilitySeries
        for series in root.findall(".//AvailabilitySeries"):
            row = {
                "ResourceID": series.findtext("ResourceID"),
                "Start": series.findtext("TimeInterval/Start"),
                "End": series.findtext("TimeInterval/End"),
                "Capacity_MW": float(series.findtext("AvailableCapacityMW")),
                "Status": series.findtext("Status")
            }
            data_rows.append(row)

        df = pd.DataFrame(data_rows)

        # Convert timestamps to datetime objects
        if not df.empty:
            df["Start"] = pd.to_datetime(df["Start"])
            df["End"] = pd.to_datetime(df["End"])

        return df