<h1 align="center">ToDosProject</h1>
<p><strong>Goal: </strong>
Create 4 positive and 4 negative automation scenarios with a hybrid test automation framework</p>
<p><strong>Demo site: </strong>
  https://todomvc.com/examples/angular2/ </p>
<p><strong>Language: </strong>
  In the Selenium Project, I am using Python language.</p>
<p><strong>Testing Framework:</strong>
  PyTest </p>
<p><strong>Type of Framework:</strong>
  I am using Data-driven Framework by using Page Object Model design pattern</p>
<p><strong>Page Objects:</strong>
As per the Page Object, I have maintained a class in the web page with the WebElements of that web page and also contains Page methods which perform operations on those WebElements.</p>
<p><strong>utilities: </strong>
 utilities package stores and handles the functions which can be commonly used across the entire framework.
</p>
<p><strong>Package: </strong>
* Selenium: Selenium Libraries
* Pytest: Python UnitedTest framework
* pytest-HTML: PyTest HTML Reports
* pyTest-xdist: Run Tests Parallel
* Openpyxl : MS Excel Support
</p>
<p><strong>Test Data: </strong>
 All the historical test data will be kept in an excel sheet. By using excel file
, I passed test data and handle data-driven testing by using “ExcelUtils.py” in utilities folder</p>
<p><strong>Configuration folder: </strong>
 Store common values such as the baseURL from ini file
</p>
<p><strong>Screenshots:  </strong>
  Screenshots will be captured and stored in a separate folder and also the screenshots of failed test cases will be added to the extent reports.</p>
<p><strong>Version Control Tool: </strong>
  I use Git as a repository to store our test scripts.
</p>

![test framework](https://user-images.githubusercontent.com/117443409/200194892-d6824502-1d67-4b4a-a75e-882479738cc2.png)

<h2 align="center">Test Scenarios</h2>
<p>
  For managing test scenarios, I am using excel to store them with the test ID. 
  It contains 4 positive and 4 negative automation scenarios for testing 4 main functions (Display func, Edit func, Todo-count func and Clear completed) in Todos list</p>



![test scenrio](https://user-images.githubusercontent.com/117443409/200196359-e895f776-c296-40fc-bca3-57051656c5a6.png)


<h2 align="center">Test HTML Report</h2>
<p>
  For the reporting purpose, I am using PyTest HTML as Test Report. It generates beautiful HTML reports. 
  It contains the test Summary information like total test cases, execution duration, and number of test cases passed, failed, errors and so on. It also contains the test Result information in details.</p>
  
![test report](https://user-images.githubusercontent.com/117443409/200196366-ec2b6b3e-d27c-4c0e-849d-d67329e2b145.png)

