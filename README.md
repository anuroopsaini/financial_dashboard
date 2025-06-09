<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 900px; margin: auto;">

  <h1 style="color:#2E86C1; text-align:center;">💸 Financial Dashboard</h1>

  <p style="font-size:1.2rem; text-align:center; color:#555;">
    Your all-in-one interactive dashboard to track, visualize, and predict personal or organizational financial flows.
  </p>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">🚀 Features</h2>
    <h3 style="color:#2874A6;">🧮 Financial KPIs</h3>
    <ul style="line-height:1.6;">
      <li>💰 <strong>Net Transaction Amount</strong></li>
      <li>📈 <strong>Average Transaction Amount</strong></li>
      <li>🟢 <strong>Total Income</strong></li>
      <li>🔴 <strong>Total Expenses</strong></li>
    </ul>
    <h3 style="color:#2874A6;">📊 Interactive Visualizations</h3>
    <ul style="line-height:1.6;">
      <li>📆 <strong>Daily Transaction Line Trends</strong></li>
      <li>🥧 <strong>Income & Expense Pie Charts</strong></li>
      <li>📅 <strong>Monthly Bar Breakdown by Category</strong></li>
      <li>💧 <strong>Waterfall Charts</strong> for Income vs Expenses</li>
      <li>📌 <strong>Dual-Axis Charts</strong> for parallel insights</li>
      <li>🔥 <strong>Heatmaps</strong> by Date and Category</li>
      <li>🧊 <strong>Bubble Charts</strong> for impact + frequency</li>
      <li>📦 <strong>Box Plots</strong> and <strong>Treemaps</strong></li>
      <li>🧭 <strong>Radar Charts</strong> for category comparison</li>
      <li>🎬 <strong>Animated Line Charts</strong> to explore patterns over time</li>
    </ul>
    <h3 style="color:#2874A6;">🔍 Smart Filtering</h3>
    <ul style="line-height:1.6;">
      <li>Filter by <strong>Category</strong></li>
      <li>Filter by <strong>Month</strong></li>
    </ul>
    <h3 style="color:#2874A6;">📈 Predictive Analytics</h3>
    <ul style="line-height:1.6;">
      <li>📉 <strong>30-Day Forecasts</strong> using linear regression</li>
      <li>📊 <strong>Confidence Intervals</strong> to assess predictive reliability</li>
    </ul>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">🛠️ Built With</h2>
    <table style="width: 100%; border-collapse: collapse; text-align: left;">
      <thead>
        <tr style="background-color:#D6EAF8;">
          <th style="padding: 10px; border: 1px solid #ccc;">Tool</th>
          <th style="padding: 10px; border: 1px solid #ccc;">Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;">🔷 <strong>Streamlit</strong></td>
          <td style="padding: 10px; border: 1px solid #ccc;">For building the interactive web UI</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;">🐼 <strong>Pandas</strong></td>
          <td style="padding: 10px; border: 1px solid #ccc;">For data manipulation and analysis</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;">📊 <strong>Altair</strong></td>
          <td style="padding: 10px; border: 1px solid #ccc;">For expressive and elegant visualizations</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;">📐 <strong>scikit-learn</strong></td>
          <td style="padding: 10px; border: 1px solid #ccc;">For implementing regression models</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;">🧵 <strong>Matplotlib</strong></td>
          <td style="padding: 10px; border: 1px solid #ccc;">Used for radar chart generation</td>
        </tr>
      </tbody>
    </table>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">📂 Dataset Requirements</h2>
    <p>The dataset should be a CSV file named:</p>
    <pre style="background-color:#f4f4f4; padding: 10px; border-radius: 5px;">filtered_financial_data.csv</pre>
    <p>and must contain the following columns:</p>
    <table style="width: 100%; border-collapse: collapse; text-align: left;">
      <thead>
        <tr style="background-color:#D6EAF8;">
          <th style="padding: 10px; border: 1px solid #ccc;">Column</th>
          <th style="padding: 10px; border: 1px solid #ccc;">Type</th>
          <th style="padding: 10px; border: 1px solid #ccc;">Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;"><code>date</code></td>
          <td style="padding: 10px; border: 1px solid #ccc;">datetime</td>
          <td style="padding: 10px; border: 1px solid #ccc;">Transaction date</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;"><code>Transaction Amount</code></td>
          <td style="padding: 10px; border: 1px solid #ccc;">float</td>
          <td style="padding: 10px; border: 1px solid #ccc;">Value of the transaction</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ccc;"><code>Category</code></td>
          <td style="padding: 10px; border: 1px solid #ccc;">string</td>
          <td style="padding: 10px; border: 1px solid #ccc;">Transaction type/category</td>
        </tr>
      </tbody>
    </table>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">📦 Installation</h2>
    <ol style="line-height:1.6;">
      <li><strong>Clone the repository:</strong>
        <pre style="background-color:#f4f4f4; padding: 10px; border-radius: 5px;">git clone https://github.com/yourusername/financial_dashboard.git
cd financial_dashboard
        </pre>
      </li>
      <li><strong>Install dependencies:</strong>
        <pre style="background-color:#f4f4f4; padding: 10px; border-radius: 5px;">pip install -r requirements.txt</pre>
      </li>
      <li><strong>Add your data file</strong> <code>filtered_financial_data.csv</code> to the root directory.</li>
      <li><strong>Run the dashboard:</strong>
        <pre style="background-color:#f4f4f4; padding: 10px; border-radius: 5px;">streamlit run dashboard.py</pre>
      </li>
    </ol>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">📌 Important Notes</h2>
    <ul style="line-height:1.6;">
      <li>✅ Ensure the CSV file is clean and formatted correctly.</li>
      <li>🚀 Streamlit caching is used for better performance.</li>
      <li>🔮 Forecasts are generated using linear regression on historical data.</li>
      <li>🧠 Confidence intervals help interpret prediction uncertainty.</li>
    </ul>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">📜 License</h2>
    <p>This project is licensed under the <strong>BSD 3-Clause License</strong>. See the <code>LICENSE</code> file for details.</p>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">🤝 Contributing</h2>
    <p>Contributions are <strong>very welcome!</strong></p>
    <ol style="line-height:1.6;">
      <li>Fork the repository</li>
      <li>Create a new branch (<code>git checkout -b feature/feature-name</code>)</li>
      <li>Make your changes</li>
      <li>Submit a pull request</li>
    </ol>
    <p>For significant changes, feel free to <a href="https://github.com/yourusername/financial_dashboard/issues" target="_blank" style="color:#2874A6;">open an issue</a> to discuss improvements.</p>
  </section>

  <hr style="border: 1px solid #ddd; margin: 20px 0;">

  <section>
    <h2 style="color:#1B4F72;">📧 Contact</h2>
    <p><strong>Anuroop Saini</strong></p>
    <p>📫 Email: <a href="mailto:anuroop193saini@gmail.com" style="color:#2874A6;">anuroop193saini@gmail.com</a></p>
    <p>🔗 LinkedIn: <a href="https://www.linkedin.com/in/anuroop-saini" target="_blank" style="color:#2874A6;">@Anuroop Saini</a></p>
  </section>

</div>
