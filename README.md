# [BMI Calculator](https://github.com/PythonDecorator)

<br />

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

--- 
![BMI Calculator.png](demo%2FBMI%20Calculator.png)
## Table of Contents

* [Overview](#overview)
* [Demo](#demo)
* [Documentation](#documentation)
* [Features](#features)
* [Flow Chart](#flow-chart)
* [Converting to Executable](#converting-to-executable)
* [Controls](#Controls)
* [Licensing](#license)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [For Open Source](#For-open-source)
* [Social Media](#Social-media)

<br />

## Overview

BMI Calculator is a user-friendly desktop application.

The purpose of this project is to create a Body Mass Index (BMI) calculator that helps users assess their health by
calculating their BMI based on their weight and height. "BMI Calculator" offers a simple and effective way for users to
monitor their health and make informed decisions about their lifestyle choices.

<br />

## Demo

![BMI App Demo.gif](demo%2FBMI%20App%20Demo.gif)

- **Download the One file .exe file from the dist folder**
- **You don't need to install anything download and start using.**

<br />

## Features

>  Some main features

1. ✅ `Friendly Interface`: An intuitive and visually appealing interface that guides users through the process
   of inputting their weight and height.

2. ✅ `BMI Calculation`: Implemented BMI formula to accurately calculate the user's Body Mass Index using their
   weight (in kilograms) and height (in meters).

3. ✅ `Result Display`: Displays the calculated BMI value along with an associated interpretation, indicating whether the
   user is underweight, normal weight, overweight, or obese.

4. ✅ `Metric and Imperial Units`: Allow users to choose between metric (kilograms and meters) and imperial (pounds and
   inches) units for inputting weight and height.

<br />

## Flow Chart
![Bmi Calculator Flowchart.png](files%2Fflow_chart%2FBmi%20Calculator%20Flowchart.png)

<br />


## Documentation

This app was built based on the customtkinter documentation

<br />

## Converting to Executable

PyInstaller is a popular tool that allows you to convert Python scripts into standalone executable files for various
platforms, effectively creating desktop applications.

- You can use PyInstaller options to customize the behavior and appearance of the generated executable. Refer to the
  PyInstaller documentation for more information on available options.
- Keep in mind that PyInstaller generates a self-contained executable, but the size of the executable might be larger
  due
  to the inclusion of the Python interpreter and any dependencies, it's best to use venv to make sure only packages used
  in the
  project are included.
- Be sure to test the generated executable on the
  target platform to ensure everything works as expected.

<br />

> Install modules via `VENV`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Create the .exe file

```bash
$ pyinstaller main.spec 
```

<br />

## Controls

- Move the slider to select your height
- Press Large plus + button to add 1 unit to the weight
- Press Large minus - button to remove 1 unit from the weight
- Press small plus + button to add 0.1 unit to the weight
- Press small minus - button to remove 0.1 unit from the weight

<br />

## License

This project is licensed under the MIT license. See also the attached LICENSE file.

<br />

## Reporting Issues

GitHub Issues is the official bug tracker for the Break-Out-II.

<br />

## Technical Support or Questions

If you have questions contact me `okpeamos.ao@gmail.com` instead of opening an issue.

- Make sure that you are using the latest version of the BMI Calculator. 
- Check the CHANGELOG
- Provide reproducible steps for the issue will shorten the time it takes for it to be fixed.

<br />

## For Open Source

"BMI Calculator" offers an excellent opportunity to create a useful and interactive desktop application for calculating
Body Mass Index. By working on this project, you'll enhance your skills in GUI development, mathematical calculations,
and user interface design. Whether you're aiming to build a tool for personal health tracking or contribute to health
awareness, "BMI Buddy" allows you to explore the world of GUI development while creating an application that promotes
health-conscious decisions.

<br />

## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---

