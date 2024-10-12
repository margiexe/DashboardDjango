const renderCharts = (data, labels) => {
    renderDoughnutChart(data, labels);
    renderBarChart(data, labels);
    renderPieChart(data, labels);
};

const renderDoughnutChart = (data, labels) => {
    var ctx = document.getElementById("doughnutChart");
    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                label: "Total cost of each service",
                data: data,
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: "Services per category (Doughnut)",
                },
            },
        },
    });
};

const renderBarChart = (data, labels) => {
    var ctx = document.getElementById("barChart");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Total cost of each service",
                data: data,
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: "Services per category (Bar)",
                },
            },
        },
    });
};

const renderPieChart = (data, labels) => {
    var ctx = document.getElementById("pieChart");
    new Chart(ctx, {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                label: "Total cost of each service",
                data: data,
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: "Services per category (Pie)",
                },
            },
        },
    });
};

const getChartData = () => {
    console.log("fetching");
    fetch("/reports-plots")
        .then((res) => res.json())
        .then((results) => {
            console.log("results", results);
            const category_data = results.category_report;
            const [labels, data] = [
                Object.keys(category_data),
                Object.values(category_data),
            ];

            renderCharts(data, labels);
        });
};

document.onload = getChartData();