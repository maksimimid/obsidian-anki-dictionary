
```dataview
TABLE   spelling as "Spelling", translation as "Translation", dateformat(striptime(Created), "yyyy-MM-dd") as "Created"
FROM #Vocabulary 
SORT  Created DESCENDING
```


