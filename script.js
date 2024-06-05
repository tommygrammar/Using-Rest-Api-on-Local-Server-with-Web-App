document.addEventListener('DOMContentLoaded', () => {
  const tableBody = document.querySelector('#ohlc-table tbody');

  fetch('/api/data') // Fetch data from the Flask endpoint
      .then(response => response.json())
      .then(data => {
          // Loop through the dates in the response data
          for (const date in data) {
              const row = tableBody.insertRow();  // Create a new table row
              const dateCell = row.insertCell();  // Create a cell for the date
              dateCell.textContent = date;       // Set the date in the cell

              // Loop through the OHLC data for this date
              const ohlcData = data[date];
              for (const value of Object.values(ohlcData)) {
                  const cell = row.insertCell();  // Create cells for OHLC
                  cell.textContent = value;       // Set the values in the cells
              }
          }
      })
      .catch(error => console.error('Error fetching data:', error));
});
