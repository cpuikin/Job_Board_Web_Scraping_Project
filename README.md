# Web_Scraping_Project

 This project is to help us understand what the job market is like. To determine the key skills necessary to get hired as a data analyst/data scientist these days. Understand what industry is currently hiring people with our skillset. Explore the different locations that we will most likely end up working in and finally I will share some fun facts.
 
 Data Collection: 
I webscraped our data from two different sources, Jobsdb and Indeed. API’s were not available for either of these sites so that wasn’t an option. I scraped all job posts that had the key word “Data” in it and I captured around 11k rows of information which was a lot. From there I did some data processing which I will talk about in a bit but I ended up with 605 Job posts from Indeed and 2042 job posts from JobsDB. For Webscraping I used Beautiful Soup and selenium and for data cleaning and plotting I used pandas, regular expression and seaborn. 

One point i want to bring up is, when I collected the data, I noticed that the Salary section was either blank or the range was ridiculously high that it didn’t make any sense. For example: I saw a company hiring a data analyst and the salary range was 20k to 90k for that specific job post. Because of this I decided to omit this column.  

After collecting the data, I merged the two datasets together. I removed any duplicates that were present. A lot of the information were piled up together so I extracted the information into desired columns using pandas and regex functions. I generated new columns counting the number of skills in each job post and counting the benefits that it offers. Finally I made sure that the data had correct types and amended as I saw fit.

After I organized and analyzed our data,  I split our findings into four main parts: Industry - Industry, Job Market, Location, and skills. We also did some online research to see if our findings and analysis are consistent with the Hong Kong job trend.  And now I start from Industry

For industry analysis, I filtered our data set and narrowed it down to see what are the top ten industries that hire the most data related talents. As you can see from the pie chart, The IT industry is in the lead with around 36 percent, which is not surprising. It makes sense that if Hong Kong wants to develop more data scientists, the industry that will lead us into this path will be from the Technology sector. However, you can see that financial services and banking are now catching up on the IT industry with around 14 percent and 13 percent respectively, slowly switching their decision making from a traditional approach to more data and technical focused. Other industries like architecture and property management that were considered traditional are also shifting. Next, I are going to dive deeper and observe the correlation of years experience with career levels and job titles across the top five industries.

On the left is the graph of average years of experience in career levels across top 5 industries. The 0 and 1,2,3 in career level stand for not specified, entry, middle, and senior level. Career level has a strong positive correlation to years of experience in general. However, the graph shows that banking and finance industries emphasize more on the years of experience when it comes to upgrading career level, so you might have to wait longer for your promotion before you hit certain years.  Whereas, IT, Human resource, and architecture industries are more flexible in years of experience in workforce which means they could focus more on the employees’ talent and skill sets. 

Moving on to the right graph is the average years of experience in job titles across industries. I narrowed down the data to the top four job titles that appear the most. Some industries do not appear on the graph because they are not hiring for the job titles that I web scrape. So from all the data that I have found, data analyst has the most consistent job hiring across industries, which requires around 3-4 years of experience. Data scientist has limited data and does not have consistency as you can see there is a high requirement for financial services but relatively little experience for banking and IT. Business analyst are somewhat consistent across industries with one year of variation except for architecture. The last is data engineer, which has large variations across industries. To wrap it up, we will very likely end up in the financial services industry if we want to become a data scientist from the start.

We went to see where most of the DATA jobs were located.
According to Indeed, that would be Kwun Tong, Kowloon Tong and Sha Tin
Whereas according to JobsDB, that would be Central and the Western area, TST as well as Sha Tin

JobsDB:
Top 3 are SQL, Python, R : totally they account for more than 70% of  top 8 skill needed
Indeed :
The same, top 3 skills are also SQL,  Python, R, accounts over 74% of top 8
And then depending on your specific job requirements or field, you can dig deeper into the other skills

Our findings regarding the skils for a DATA job is in line with our online research that you can see on this slide.  You may have noticed that VBA is a skill still in demand, perhaps that is because many companies are using Excel...

This picture is filtered by Data Analyst Scientist, Engineer, Business Analyst, System Analyst, Business Intelligence, Quant Analyst, IT Analyst
Exp is Less than 5 years
Career Level set on Entry and Medium

In this year, the covid-19 pandemic ,many companies suggest employer Work from home.
But in IT industry, NOT everyone can.
If you Really love WFH, perhaps you should focus on Data Engineer or System Analyst
not feel sad on the company not allow work from home, i show u something .
Look at this graph, you can see only system analyst and business intelligence have transportation allowance
But a good news,  more company provide FREE shuttle bus, Is it give you one more reason back to office?
