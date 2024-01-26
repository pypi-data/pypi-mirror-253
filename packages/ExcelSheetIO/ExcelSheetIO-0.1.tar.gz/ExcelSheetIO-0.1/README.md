# ExcelSheetIO

A Python package for efficient Excel sheet operations. Enables easy read/write functionality, data manipulation, and workflow automation. Ideal for handling both small and large datasets. Get started with ExcelSheetIO for a simplified data processing experience.

## ExcelReaderWriter Usage Guide

The `ExcelReaderWriter` class in Python provides an efficient way to read and retrieve data from Excel sheets. This guide will help you understand how to use the `getTestData` method in this class.

Sure, here's a more refined explanation:

![ExcelSheet](/assets/img/excel_clip.png "excel logo")

To use the `getTestData` method in Python, you need to identify the specific cell data you want to read. Let's say, for example, you want to read the cell value `Sr. Analyst` from an Excel sheet.

First, identify the sheet that contains the data you're looking for. In this case, the sheet name is `Sheet1`.

Next, determine the row where your data resides. In this example, `Sr. Analyst` is in row number `6`. To better identify the row, we use the data from the first row as a unique identifier.

Then, identify the column that contains your data. In this scenario, the column header name is `Job Title`.

With these parameters - the sheet name, the unique identifier from the first row, and the column header name - you can use the `getTestData` method to read the data. The syntax would be:

```python
data = excel_reader_writer.getTestData('SheetName', 'UniqueIdentifier', 'ColumnHeaderName')
```

In this code, replace `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with your actual values (`Sheet1`, `Row_data_of_right_most_column`, and `Job Title`, respectively) when you use this method. This will return the data from the specified cell.


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

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'TestCaseName'`, and `'ColumnName'` with the path to your Excel file, the name of the sheet in the Excel file, the name of the test case, and the name of the column, respectively.

## Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `getTestData` method. Here's how you can do it:

```robotframework
*** Settings ***
Library           ExcelSheetIO.ExcelReaderWriter    relative_relative_path_to_your_excel_file

*** Keywords ***
Testcase for read data
    [Arguments]
    ${data}=    Get Test Data    ${sheetName}    ${UniqueIdentifier}    ${ColumnHeaderName}
    [Return]    ${data}

*** Test Cases ***
Test Case 1
    ${data}=    Testcase for read data
    Log    ${data}
```

In the above code, replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with the path to your Excel file, the name of the sheet in the Excel file, the name of the test case, and the name of the column, respectively.

Please replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifier'`, and `'ColumnHeaderName'` with your actual values when you use this code.

