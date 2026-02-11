</head>

<body>

<div class="container">

<h1>House Price Prediction Project</h1>
<p style="text-align:center;"><strong>Project By:</strong> G. Krishna<br>
Last Updated: 11-02-2026</p>

<div class="box">
<h2>1. Project Overview</h2>
<p>
This project develops a machine learning web application that predicts house prices 
based on multiple property features. The model is trained using historical housing data 
and deployed using Flask and Render.
</p>
</div>

<div class="box">
<h2>2. Dataset Description</h2>
<ul>
<li><strong>Dataset:</strong> House Sales in King County, USA</li>
<li><strong>Total Records:</strong> 21,613 houses</li>
<li><strong>Time Period:</strong> May 2014 – May 2015</li>
<li><strong>Location:</strong> King County, Washington</li>
</ul>

<h3>Features Used (17 Inputs)</h3>
<ul>
<li>Bedrooms</li>
<li>Bathrooms</li>
<li>Sqft Living</li>
<li>Sqft Lot</li>
<li>Floors</li>
<li>Waterfront</li>
<li>View</li>
<li>Condition</li>
<li>Sqft Above</li>
<li>Sqft Basement</li>
<li>Year Built</li>
<li>Year Renovated</li>
<li>City (Encoded)</li>
<li>Country (Encoded)</li>
<li>Year</li>
<li>Month</li>
<li>Day</li>
</ul>
</div>

<div class="box">
<h2>3. Technology Stack</h2>
<ul>
<li><strong>Backend:</strong> Python, Flask</li>
<li><strong>Machine Learning:</strong> Scikit-learn, NumPy, Pandas</li>
<li><strong>Frontend:</strong> HTML, CSS</li>
<li><strong>Deployment:</strong> Render</li>
<li><strong>Version Control:</strong> Git & GitHub</li>
</ul>
</div>

<div class="box">
<h2>4. Implementation Steps</h2>
<h3>Step 1: Data Preprocessing</h3>
<ul>
<li>Handle missing values</li>
<li>Extract year, month, day from date column</li>
<li>Encode categorical features (city, country)</li>
<li>Split data into training and testing sets</li>
</ul>

<h3>Step 2: Model Training</h3>
<ul>
<li>Linear Regression Model</li>
<li>Train using 80% data</li>
<li>Test using 20% data</li>
<li>Evaluate using RMSE and R² score</li>
</ul>

<h3>Step 3: Save Model</h3>
<ul>
<li>Model saved using pickle (.pkl file)</li>
</ul>

<h3>Step 4: Flask Application</h3>
<ul>
<li>Create routes for home and prediction</li>
<li>Collect form inputs</li>
<li>Convert inputs to float</li>
<li>Predict house price</li>
</ul>
</div>

<div class="box">
<h2>5. Model Development</h2>
<p>
The project uses Linear Regression as the prediction algorithm. 
It calculates coefficients using matrix operations and evaluates performance using:
</p>
<ul>
<li>R² Score</li>
<li>Mean Squared Error (MSE)</li>
<li>Root Mean Squared Error (RMSE)</li>
</ul>
</div>

<div class="box">
<h2>6. Deployment Process</h2>
<ul>
<li>Upload project to GitHub</li>
<li>Create Web Service in Render</li>
<li>Set build command: pip install -r requirements.txt</li>
<li>Set start command: gunicorn app:app</li>
<li>Deploy and access live URL</li>
</ul>
</div>

<div class="box">
<h2>7. Sample Prediction</h2>
<p><strong>Input Example:</strong></p>
<ul>
<li>Bedrooms: 2</li>
<li>Bathrooms: 2</li>
<li>Sqft Living: 300</li>
<li>Sqft Lot: 300</li>
<li>Floors: 3</li>
<li>Waterfront: 0</li>
<li>View: 4</li>
<li>Condition: 4</li>
<li>Sqft Above: 300</li>
<li>Sqft Basement: 300</li>
<li>Year Built: 2000</li>
<li>Year Renovated: 2000</li>
<li>City: 8</li>
<li>Country: 0</li>
<li>Year: 1990</li>
<li>Month: 12</li>
<li>Day: 12</li>
</ul>

<p><strong>Output:</strong> Estimated House Price: 417322.15</p>
</div>

<div class="box">
<h2>8. Challenges and Solutions</h2>
<ul>
<li>Encoding categorical features</li>
<li>Handling string inputs from HTML forms</li>
<li>Deployment dependency issues</li>
<li>Model serialization using pickle</li>
</ul>
</div>

<div class="box">
<h2>9. Future Enhancements</h2>
<ul>
<li>Implement Random Forest & Gradient Boosting</li>
<li>Add data visualization charts</li>
<li>Store prediction history in database</li>
<li>Deploy using Docker</li>
<li>Add monitoring & logging</li>
</ul>
</div>

<div class="box">
<h2>10. Conclusion</h2>
<p>
This project demonstrates a complete end-to-end machine learning pipeline 
from data preprocessing to deployment. It provides real-time house price 
predictions through a user-friendly web interface.
</p>
</div>

<div class="footer">
© 2026 G. Krishna | House Price Prediction Project
</div>

</div>

</body>
</html>
