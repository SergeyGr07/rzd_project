// Fetch data from the server
fetch('/data')
  .then(response => response.json())
  .then(data => {
    // Get table elements
    const tableHeader = document.getElementById('table-header');
    const tableBody = document.getElementById('table-body');

    // Create table headers
    for (const key in data[0]) {
      const th = document.createElement('th');
      th.textContent = key;
      tableHeader.appendChild(th);
    }

    // Create table data
    for (const item of data) {
      const tr = document.createElement('tr');
      for (const key in item) {
        const td = document.createElement('td');
        td.textContent = item[key];
        tr.appendChild(td);
      }
      tableBody.appendChild(tr);
    }
  });
