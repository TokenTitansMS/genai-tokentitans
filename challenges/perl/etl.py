import csv

TABLE_NAME = 'nasdaq_prices'
DATABASE_ENGINE = 'InnoDB'
DEFAULT_CHARSET = 'latin1'

filename = 'prices.csv'
schema_file = "mysqlCreateSchemaPy.sql"
values_file = "mysqlInsertValuesPy.sql"

def etl_process(filename, schema_file, values_file):

    with open(schema_file, 'w') as schema, open (values_file, 'w') as values:
        
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)

            headers = [header.replace("'", "\\'").replace('\"', '').replace(' ', '_') for header in headers]
            column_headers = ', '.join(headers)
            header_count = len(headers)
            
            field_types = ["varchar"] * header_count
            field_lengths = [0] * header_count
            decimal_lengths = [(0, 0)] * header_count
            
            row_count = 0
            
            for row in reader:
                row_count += 1
                for i, value in enumerate(row):
                    if value.isdigit():
                        if field_types[i] != "decimal":
                            field_types[i] = "int"
                        field_lengths[i] = max(field_lengths[i], len(value))
                    elif value.replace(".", "", 1).isdigit():
                        field_types[i] = "decimal"
                        int_part, _, frac_part = value.partition(".")
                        decimal_lengths[i] = (
                            max(decimal_lengths[i][0], len(int_part)),
                            max(decimal_lengths[i][1], len(frac_part)),
                        )
                    else:
                        field_types[i] = "varchar"
                        field_lengths[i] = max(field_lengths[i], len(value))
                    
                row_values = [f"'{value}'" if value else "'0'" for value in row]
                values.write(f"INSERT INTO {TABLE_NAME} ({column_headers})\n")
                values.write(f"VALUES ({', '.join(row_values)});\n")
                
            csvfile.close()
            
            schema.write(f"CREATE TABLE `{TABLE_NAME}` (\n")
            for i, header in enumerate(headers):
                if field_types[i] == "decimal":
                    schema.write(
                        f"  `{header}` {field_types[i]}({decimal_lengths[i][0] + decimal_lengths[i][1]},{decimal_lengths[i][1]})"
                    )
                else:
                    schema.write(f"  `{header}` {field_types[i]}({field_lengths[i]})")
                if i < len(headers) - 1:
                    schema.write(",\n")
            schema.write(f"\n) ENGINE={DATABASE_ENGINE} DEFAULT CHARSET={DEFAULT_CHARSET};\n")

            print(f"Processed {header_count} columns and {row_count} lines.")
        
        schema.close()
        values.close()
        
if __name__ == "__main__":
    etl_process(filename, schema_file, values_file)