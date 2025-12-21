from src.parser import BDEWParser
import sys

def main():
    # Configuration paths
    XML_FILE = "data/sample_redispatch.xml"
    XSD_FILE = "data/schema.xsd"

    print("--- BDEW Redispatch 3.0 Parser Tool ---")

    try:
        # Initialize Parser
        parser = BDEWParser(schema_path=XSD_FILE)

        # Step 1: Validate
        if parser.validate(XML_FILE):

            # Step 2: Parse
            df = parser.parse_to_dataframe(XML_FILE)

            # Step 3: Display Analysis
            print("\n--- Parsed Data (First 5 Rows) ---")
            print(df.head())

            print("\n--- Summary Statistics ---")
            print(f"Total Average Capacity: {df['Capacity_MW'].mean():.2f} MW")
            print(f"Data Entries: {len(df)}")

            # Optional: Save to CSV
            output_file = "redispatch_output.csv"
            df.to_csv(output_file, index=False)
            print(f"\nData exported to {output_file}")

        else:
            print("Skipping parsing due to validation errors.")
            sys.exit(1)

    except Exception as e:
        print(f"Critical Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()