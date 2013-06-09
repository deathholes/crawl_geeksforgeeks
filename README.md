This is a simple crawler to download all the html pages from the site:
"www.geeksforgeeks.org".
Many things are hard coded in it and it only saves the html texts at 
present. Any CSS, JavaScript or images are not saved. 
This was made by me for saving the pages for offline usage. Most 
probably no more commits will be made on his repo, but there will be 
another repo coming with changes.

Summary of the Project:
-- crawler for the site "www.geeksforgeeks.org"
-- sequential web crawler
-- saves only texts
-- does not save images, scripts, etc.
-- only links to the same site are saved i.e, external links are not  
  entertained.
-- filename corresponds to the last phrase of the link i.e for 
	www.geeksforgeeks.org/tag/dynamic-programming will be saved as:
	dynamic-programming
-- coded in python 3.2
