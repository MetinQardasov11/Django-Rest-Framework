const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {

    if (xhr.readyState === 4 && xhr.status === 200) {

        const data = JSON.parse(xhr.responseText);
        const tableBody = document.querySelector('#data-table tbody');
        data.forEach(item => {

            const row = document.createElement('tr');
            row.innerHTML = `<td>${item.name}</td><td>${item.email}</td>`;
            tableBody.appendChild(row);

        });
    }
};

xhr.open('GET', 'API/data.json', true);

xhr.send();