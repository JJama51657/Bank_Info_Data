<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>High-Value Transaction Detection Project</title>
</head>
<body>
  <h1>High-Value Transaction Detection Project</h1>

  <p>This project tracks the full data pipeline from raw data processing to final visualization, using Python, SQL, Excel, and Power BI.</p>

  <h2>Project Overview</h2>
  <ul>
    <li><strong>Objective:</strong> Detect unusually large financial transactions by comparing each transaction against the average for its channel (ATM, Branch, Online).</li>
    <li><strong>Tools Used:</strong> Python, SQL, Excel, Power BI</li>
    <li><strong>Focus Areas:</strong> Data Cleaning, Data Integration, Anomaly Detection, Business Insights</li>
  </ul>

  <h2>Steps and Technologies</h2>
  <ul>
    <li><strong>Python:</strong>
      <ul>
        <li>Imported raw transaction data (CSV files).</li>
        <li>Performed initial data cleaning: removed duplicates, handled missing values, standardized date formats.</li>
        <li>Exported cleaned datasets for SQL processing.</li>
      </ul>
    </li>
    <li><strong>SQL:</strong>
      <ul>
        <li>Created a transactional database structure.</li>
        <li>Aggregated transaction amounts by channel to compute average values.</li>
        <li>Performed INNER JOIN between transaction records and channel statistics.</li>
        <li>Flagged transactions significantly higher than their channel's average.</li>
      </ul>
    </li>
    <li><strong>Excel:</strong>
      <ul>
        <li>Loaded cleaned and joined data into Excel for validation and exploratory analysis.</li>
        <li>Created pivot tables and basic charts to check data integrity and identify early patterns.</li>
      </ul>
    </li>
    <li><strong>Power BI:</strong>
      <ul>
        <li>Built an interactive dashboard showcasing high-value transactions.</li>
        <li>Visualized transaction amounts by channel and flagged anomalies.</li>
        <li>Added filters for dynamic exploration by transaction type, channel, and time period.</li>
      </ul>
    </li>
  </ul>

  <h2>Key Results</h2>
  <ul>
    <li>Identified outlier transactions that may indicate fraud, VIP customers, or operational issues.</li>
    <li>Provided visual tools for business stakeholders to monitor transaction patterns across channels.</li>
  </ul>

  <h2>Skills Demonstrated</h2>
  <ul>
    <li>Data Cleaning and Preprocessing</li>
    <li>SQL Joins and Aggregations</li>
    <li>Data Validation in Excel</li>
    <li>Dashboard Design and Visualization in Power BI</li>
    <li>End-to-End Data Pipeline Development</li>
  </ul>

</body>
</html>
