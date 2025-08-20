# 🚀 3D Data Science Workbench

Welcome to the 3D Data Science Workbench – your interactive playground for exploring, visualizing, and manipulating datasets in 3D! 🎉

This app lets you upload CSV files, visualize them in interactive 3D charts, run statistical analyses, and even manipulate data on the fly with live JavaScript coding.

✨ Features
📊 3D Data Visualization

View your selected numerical feature as interactive 3D bars.

Rotate, zoom, and explore your data in real time.

Dynamic coloring and height scaling for easy interpretation.

📈 Advanced Data Analysis

Boxplots: Compare distributions across features.

Correlation Matrix: Discover relationships between variables.

Scatter Plot Matrix: Visualize pairwise relationships.

PCA Plot: Perform dimensionality reduction and explore patterns.

Distribution Fitting: Analyze and fit distributions to your features.

💻 Live Coding Environment

Write JavaScript to manipulate your dataset (modifiedData).

Use output.push("message") to log messages.

Transform, filter, or create new features – visualization updates instantly.

🖱️ Interactive Controls

Resizable left panel (drag or double-click to collapse/expand).

Feature selectors for visualization and analysis.

Real-time updates as you tweak your data.

🏁 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/3d-data-science-workbench.git
cd 3d-data-science-workbench

2️⃣ Install Dependencies
npm install

3️⃣ Run the App
npm start


Then open http://localhost:3000/
 in your browser 🎨

📂 Project Structure
src/
├── App.tsx               # Main entry point
├── Boxplot.tsx           # Boxplot visualization
├── CorrelationMatrix.tsx # Correlation heatmap
├── ScatterPlotMatrix.tsx # Pairwise scatter plots
├── StatsTable.tsx        # Statistical summary
├── PCAPlot.tsx           # PCA visualization
├── DistributionFit.tsx   # Distribution analysis
├── App.css               # Styling

📌 Usage

Upload a CSV File

Click the Upload Data button.

Make sure the first row contains headers.

Choose a Feature to Visualize in 3D

Select a numerical feature from the dropdown.

Spin and explore the 3D bars.

Explore Analysis

Select multiple features for advanced analysis.

View correlations, PCA, scatter plots, and more.

Start Coding!

Write JavaScript in the coding environment.

Example:

modifiedData.forEach(row => {
  row.DoubleValue = parseFloat(row.SomeFeature) * 2;
});
output.push("Created a new feature: DoubleValue!");


Run your code and see the visualization update instantly.

🛠️ Built With

React + TypeScript – Frontend framework

Three.js – 3D visualizations

Chart.js & Custom SVGs – Charts & plots

PapaParse – CSV parsing

🎯 Who Is This For?

Students learning about data visualization

Data enthusiasts who want to explore datasets quickly

Researchers testing hypotheses

Anyone who thinks 3D data looks cool 😎

🐛 Troubleshooting

Refresh the page if something breaks.

Make sure your CSV has headers.

Use numerical columns for visualization.

📜 License

MIT License © 2025
