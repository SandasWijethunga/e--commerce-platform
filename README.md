### WAN Pizza – Cloud-Based E-Commerce Application

WAN Pizza is a scalable, cloud-native e-commerce platform built to provide users with a seamless digital pizza ordering experience. The system leverages a serverless architecture on AWS to ensure high performance, cost-efficiency, and automatic scalability.

🍕 Project Overview
* Module: Cloud Computing for data science 
* Objective: To demonstrate a robust and resilient deployment of a commercial web application using modern cloud infrastructure.
* Core Functionality: Users can browse a digital menu, personalize their pizza selections, and place orders through a web interface.

🏗️ Architecture Design
* The application utilizes a fully serverless stack to minimize operational complexity and overhead:
* Frontend: Static HTML pages (e.g., order.html, success.html) served via Lambda or optionally hosted on S3.
* API Exposure: Amazon API Gateway acts as the entry point, connecting client requests to backend logic.
* Compute: AWS Lambda handles backend logic, including processing GET requests to serve the menu and POST requests to handle orders.
* Database: Amazon DynamoDB (NoSQL) provides on-demand storage for order data, using email as the partition key.
* Monitoring: AWS CloudWatch is used for logging, diagnostics, and tracing errors.

🛠️ Tech Stack & Tools
* Cloud Provider: Amazon Web Services (AWS) 
* Backend Language: Python (boto3 SDK) 
* Database: Amazon DynamoDB 
* Infrastructure: AWS Lambda, API Gateway, S3, and RDS (for structured data)

🚀 Key Features
* Serverless Execution: Charges are only incurred per invocation, keeping costs minimal.
* On-Demand Scaling: DynamoDB and Lambda automatically scale based on traffic volume.
* Security: Secured via IAM roles and policies to restrict permissions between services.
* Data Protection: Supports point-in-time recovery for disaster recovery

📂 Project Structure
* lambda_function.py: The core Python logic for handling HTTP methods and DynamoDB integration.
* order.html: The main customer-facing pizza store interface.
* success.html: The confirmation page shown after a successful order.
* report of project.pdf: Full documentation covering the implementation and cost analysis.

🔮 Future Enhancements
* Implementation of user authentication via Amazon Cognito.
* Development of a dynamic frontend using React or Vue.js.
* Integration of an Admin Dashboard for sales analytics.
* Automated email notifications for order receipts.
