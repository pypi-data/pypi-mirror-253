# ExcelSheetIO

A Python package for efficient Excel sheet operations. Enables easy read/write functionality, data manipulation, and workflow automation. Ideal for handling both small and large datasets. Get started with ExcelSheetIO for a simplified data processing experience.

## Installation Guide

```python
pip install ExcelSheetIO
```

## `Read Data From Excel Sheet`

The `ExcelReaderWriter` class in Python provides an efficient way to read and retrieve data from Excel sheets. This guide will help you understand how to use the `getTestData` method in this class.

Sure, here's a more refined explanation:

![ExcelSheet](/assets/img/excel_clip.png "excel logo")

To use the `getTestData` method in Python, you need to identify the specific cell data you want to read. Let's say, for example, you want to read the cell value `Sr. Analyst` from an Excel sheet.

First, identify the sheet that contains the data you're looking for. In this case, the sheet name is `Sheet1`.

Next, determine the row where your data resides. In this example, `Sr. Analyst` is in row number `6`. To better identify the row, we use the data from the first column as a unique identifier(make sure the data of the 1st column of the sheet should be uniquely identifier data).

Then, identify the column header that contains your data. In this scenario, the column header name is `Job Title`.

With these parameters - the sheet name, the unique identifier from the first column, and the column header name - you can use the `getTestData` method to read the data. The syntax would be:

```python
data = excel_reader_writer.getTestData('SheetName', 'UniqueIdentifier', 'ColumnHeaderName')
```

In this code, replace `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with your actual values (`Sheet1`, `E5`, and `Job Title`, respectively) when you use this method. This will return the data from the specified cell.

### Python Usage

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the getTestData method
data = excel_reader_writer.getTestData('SheetName', 'UniqueIdentifier', 'ColumnHeaderName')

# Print the retrieved data
print(data)
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnName'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, and the name of the column header, respectively.

### Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `getTestData` method. Here's how you can do it:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    relative_path_to_your_excel_file

*** Keywords ***
Keyword For Read Excel Sheet Data
    [Arguments]    ${sheetName}    ${UniqueIdentifier}    ${ColumnHeaderName}
    ${data}=    Get Test Data    ${sheetName}    ${UniqueIdentifier}    ${ColumnHeaderName}
    Log To Console    ${\n}${data}

*** Test Cases ***
Test case for read data from excel sheet
    [Tags]    read     test
    Keyword For Read Excel Sheet Data    SheetName    UniqueIdentifier    ColumnHeaderName
```

In the above code, replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, and the name of the column header, respectively.

Please replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with your actual values (`.\\Data\\Employee.xlsx`, `Sheet1`, `E5`, and `Job Title`, respectively) when you use this code.

## `Write Data From Excel Sheet`

The `ExcelReaderWriter` class in Python provides an efficient way to read and write data to Excel sheets. This guide will help you understand how to use the `setTestData` method in this class.

To use the `setTestData` method in Python, you need to identify the specific cell where you want to write data. Let's say, for example, you want to write the value `Sr. Analyst` into a cell in an Excel sheet.

First, identify the sheet where you want to write the data. In this case, the sheet name is `Sheet1`.

Next, determine the row where you want to write your data. In this example, `Sr. Analyst` is to be written in row number `6`. To better identify the row, we use the data from the first column as a unique identifier (make sure the data of the 1st column of the sheet should be uniquely identifier data).

Then, identify the column header where you want to write your data. In this scenario, the column header name is `Job Title`.

Finally, determine the data you want to write. In this case, the data is `Sr. Analyst`.

With these parameters - the sheet name, the unique identifier from the first column, the column header name, and the data to be written - you can use the `setTestData` method to write the data. The syntax would be:

```python
excel_reader_writer.setTestData('SheetName', 'UniqueIdentifier', 'ColumnHeaderName', 'WritableData')
```

In this code, replace `'SheetName'`, `'UniqueIdentifier'`, `'ColumnHeaderName'`, and `'WritableData'` with your actual values (`Sheet1`, `E5`, `Job Title`, and `Sr. Analyst`, respectively) when you use this method. This will write the data into the specified cell. Please ensure that you have write permissions for the Excel file.

### Python Usage

Here's how you can use the `setTestData` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the setTestData method
excel_reader_writer.setTestData('SheetName', 'UniqueIdentifier', 'ColumnHeaderName', 'WritableData')
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, `'ColumnHeaderName'`, and `'WritableData'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, the name of the column header, and the order number, respectively.

### Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `setTestData` method. Here's how you can do it:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    path_to_your_excel_file

*** Keywords ***
Set Test Data
    [Arguments]    ${sheetName}    ${UniqueIdentifier}    ${ColumnHeaderName}    ${WritableData}
    Set Test Data    ${sheetName}    ${UniqueIdentifier}    ${ColumnHeaderName}    ${WritableData}

*** Test Cases ***
Test Case 1
    Set Test Data    SheetName    UniqueIdentifier    ColumnHeaderName    WritableData
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, `'ColumnHeaderName'`, and `'WritableData'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, the name of the column header, and the order number, respectively.

Please replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, `'ColumnHeaderName'`, and `'WritableData'` with your actual values (`.\\Data\\Employee.xlsx`, `Sheet1`, `E5`, `Job Title` and `Sr. Analyst`, respectively) when you use this code.

### Breakdowns

Let's break down how the `setTestData` method works internally, in a more understandable way :

**`Creating a Copy`** : The method starts by creating a copy of the original Excel file. This is done to ensure that the original file remains unchanged until all write operations are successfully executed. The copy is stored in a folder named 'CopyFolder' and is given a temporary name like '*_Temp*.xlsx'.

**`Writing Data`** : The method then performs the write operation on this temporary Excel file. It writes data to a specific cell in an Excel sheet. The cell is identified by the sheet name, the unique identifier from the first column (which should be unique), and the column header name.

**`Saving Changes`** : After all write operations are completed, the method saves the changes made to the temporary file.

**`Updating the Original File`** : The method then transfers the data from the temporary file back into the original file. This ensures that the original file is updated with all the new data.

**`Cleaning Up`** : Finally, the method removes the temporary Excel file after all operations are finished. This is done to free up storage space and maintain cleanliness in your file system.

By using this method, you can efficiently write data to an Excel file while ensuring the integrity of the original file until all operations are successfully completed. It's a safe and efficient way to manipulate Excel data in Python. Please ensure that you have write permissions for the Excel file.