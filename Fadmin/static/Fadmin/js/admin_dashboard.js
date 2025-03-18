  

  // Initialize Course Enrollments Chart
  const ctx = document.getElementById('coursesChart').getContext('2d');
  
  const chartData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [
      {
        label: 'Web Development',
        data: [65, 78, 90, 85, 92, 110],
        backgroundColor: '#1a56db',
        borderColor: '#1a56db',
        borderWidth: 2,
        borderRadius: 5,
        barPercentage: 0.6,
      },
      {
        label: 'Data Science',
        data: [45, 55, 65, 85, 98, 120],
        backgroundColor: '#e53e3e',
        borderColor: '#e53e3e',
        borderWidth: 2,
        borderRadius: 5,
        barPercentage: 0.6,
      }
    ]
  };
  
  const chartConfig = {
    type: 'bar',
    data: chartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          align: 'end',
          labels: {
            boxWidth: 15,
            usePointStyle: true,
            pointStyle: 'circle'
          }
        },
        tooltip: {
          backgroundColor: 'rgba(255, 255, 255, 0.9)',
          titleColor: '#718096',
          bodyColor: '#4a5568',
          borderColor: '#e2e8f0',
          borderWidth: 1,
          padding: 10,
          boxPadding: 5,
          usePointStyle: true,
          callbacks: {
            labelPointStyle: function() {
              return {
                pointStyle: 'circle',
                rotation: 0
              };
            }
          }
        }
      },
      scales: {
        x: {
          grid: {
            display: false
          }
        },
        y: {
          beginAtZero: true,
          grid: {
            color: '#f0f2f5'
          },
          ticks: {
            stepSize: 30
          }
        }
      }
    }
  };
  
  const coursesChart = new Chart(ctx, chartConfig);
  
  // Menu item click event
  const menuItems = document.querySelectorAll('.menu-item');
  menuItems.forEach(item => {
    item.addEventListener('click', () => {
      menuItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');
    });
  });
  
  // Filter button click event
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
