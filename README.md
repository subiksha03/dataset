According to the statistics, in the first half of 2022, there were 236.1 million ransomware attempts. Ransomware, a type of malware whose primary objective is to encrypt important files and render the victim's system inoperable before demanding payment to undo the damage, accounts for a significant portion of these incidents. As a result of their sophisticated packing methods, some ransomware is difficult to statically analyze. The system proposed, a machine learning strategy for dynamically analyzing and classifying ransomware, is what we present here. The proposed system screens a set of activities performed by applications in their most memorable periods of establishment checking for qualities that are indications of ransomware. This system achieves a high accuracy in our tests on a dataset of 61 benign files applications and 86 ransomwares belonging to various families. Additionally, this system operates without requiring the availability of the entire ransomware family beforehand. Since ransomware samples exhibit a set of characteristic features at run-time that are common across families, these findings suggest that dynamic analysis can support ransomware detection. This aids in the early detection of ransomware. The proposed model has achieved 95% accuracy with Random Forest classifier.

The data of 61 benign files and 86 ransomware files which totals to 147 samples was processed. The label field (class = 0 for benign files and 1 for ransomware) is added. Finally, utilized these 15 selected features to provide to the machine learning classifiers to classify  ransomware and benign files.

Category	 |    Features Selected 

API CALLS	  |   advapi32.dll, user32.dll, kernel32.dll, mpr.dll, comctl32.dll, msvcrt.dll

STRINGS	     |   bitcoin, mscoree.dll, COMDLG32.dll, onion

EMBEDDED
EXECUTABLE   |  
FILES	           RT_RCDATA, RT_ICON, RT_GROUP_ICON, RT_VERSION_INFO

Entropy	     |    Value Greater than 7

DNS Requests	 |  Value greater than 30 in 10 seconds

