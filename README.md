# bigfish

Simple automation script for webbrowser game

## Getting started

### Prerequisites

Python 3

### Installation instructions

Clone repository and Install requirements.txt:

```
git clone https://github.com/tvturnhout/bigfish
cd bigfish
pip install requirements.txt
```

Make sure you have Chrome installed and download latest chromedriver from [here](http://chromedriver.chromium.org/downloads).
Save the chromedriver.exe and add to PATH with the following instructions:

1. On the Windows desktop, right-click My Computer.
2. In the pop-up menu, click Properties.
3. In the System Properties window, click the Advanced tab, and then click Environment Variables.
4. In the System Variables window, highlight Path, and click Edit.
5. In the Edit System Variables window, insert the cursor at the end of the Variable value field.
6. If the last character is not a semi-colon (;), add one.
7. After the final semi-colon, type the full path to the file you want to find. (For example: path C:\folder_that_contains_chromedriver)
8. Click OK in each open window.

### Parameters

PATH_TO_USER_DATA should point to your Chrome user data. You can find this path as following:

![](https://www.howtogeek.com/wp-content/uploads/2016/05/x02_typing_chrome_version.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.8xEaB4Bxoa.png)
![](https://www.howtogeek.com/wp-content/uploads/2016/05/x03_profile_path_for_work_profile.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.KLISGMdQa-.png)

### Notes

Make sure you run with admin rights.
