# Hawaiian Temperature Analysis
Author: Jeff Gielniak
Date: 2025-02-07    

I used SQLAlchemy to take weather data from various weather stations in Hawaii.  The data was cleaned, sorted and used to make visualizations.  We then used Flask to create a webpage with API routes for user interaction with various information from the dataset.

-The app.py folder is my python code to create the Climate App.  The code will guide you to a homepage that will list 5 options to navigate to for different information:
1. Precipitation analysis for the last year of data in the Hawaii.sqlite database
2. A list of the stations in that show up in the data
3. A list of dates and temps from the most active station in the previous year from the data
4. The Temperature Min, Max and Average if you supply a start date
5. The Temperature Min, Max and Average if you supply a start and end date
<img width="775" alt="Screenshot 2025-03-28 at 11 48 40 AM" src="https://github.com/user-attachments/assets/bc9b7fee-adcb-45fc-ad9d-2a9cb3db4807" />
<img width="945" alt="Screenshot 2025-03-28 at 11 48 30 AM" src="https://github.com/user-attachments/assets/b710124e-21ad-46b5-a02b-3834dad597aa" />
<img width="764" alt="Screenshot 2025-03-28 at 11 48 15 AM" src="https://github.com/user-attachments/assets/4807d363-2866-43b8-bf08-092cb577cfa7" />
<img width="1436" alt="Screenshot 2025-03-28 at 11 49 54 AM" src="https://github.com/user-attachments/assets/9e39bb58-bc16-4a2c-8b72-97ac45b62a37" />
