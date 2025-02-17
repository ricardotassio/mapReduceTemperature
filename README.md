Here's a sample README file for your Python script:

---

# MapReduce Temperature Processor

This Python script processes temperature data from multiple CSV files, using a MapReduce approach to determine the highest temperature recorded for each city. The script reads the data, maps the city-temperature pairs, and reduces the data to find the highest temperature for each city.

## Files

- `temp1.csv`, `temp2.csv`, `temp3.csv`: Input CSV files containing temperature data for various cities. Each file should follow the format:

  ```
  City,Temperature
  City1,Temp1
  City2,Temp2
  ...
  ```

- `highest_temperature.csv`: Output CSV file generated by the script, containing the highest temperature recorded for each city.

## Script Overview

### `map_files(input_files: list) -> list`

- **Description**:
  This function takes a list of input CSV files, reads each file, and maps the city and temperature data into a list of tuples.
- **Parameters**:
  - `input_files`: A list of filenames (strings) to be processed.
- **Returns**:
  A list of tuples in the format `(city, temperature)`.

### `reduce(mapped_file: list) -> dict`

- **Description**:
  This function reduces the mapped data to find the highest temperature for each city and writes the result to an output CSV file (`highest_temperature.csv`).
- **Parameters**:
  - `mapped_file`: A list of tuples in the format `(city, temperature)` produced by the `map_files` function.
- **Returns**:
  A dictionary with cities as keys and their highest recorded temperatures as values.

### Main Execution

- The script runs the `map_files` function on the provided CSV files, followed by the `reduce` function to determine and output the highest temperatures for each city.
- The result is printed to the console and saved to `highest_temperature.csv`.

## Usage

1. Ensure your input CSV files (`temp1.csv`, `temp2.csv`, `temp3.csv`) are in the same directory as the script.
2. Run the script using Python:
   ```bash
   python mapreduce_temperature.py
   ```
3. The script will output a file named `highest_temperature.csv` containing the highest temperature recorded for each city.

## Example

Given the following input files:

**temp1.csv**

```
city, temperature
Toronto,10
Ottawa,15
Montreal,12
Vancouver,8
```

**temp2.csv**

```
city, temperature
Toronto,15
Ottawa,6
Montreal,10
Vancouver,13

```

**temp3.csv**

```
city, temperature
Toronto,23
Ottawa,1
Montreal,5
Vancouver,1
```

The script will produce the following output in `highest_temperature.csv`:

```
City,Temperature
Toronto,23
Ottawa,15
Montreal,12
Vancouver,13
```

## Requirements

- Python 3.x
- Standard Python libraries: `csv`
