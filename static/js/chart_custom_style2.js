/*------------------------------------------------------------------
    File Name: chart_custom_style2.js
    Template Name: Pluto - Responsive HTML5 Template
    Created By: dashboard.design
    Envato Profile: https://themeforest.net/user/htmldotdesign
    Website: https://html.design
    Version: 1.0
-------------------------------------------------------------------*/

var presets = window.chartColors;


		new Chart('chart-2', {
				type: 'line',
				data: {
					labels: document.getElementById('upload_months').value.split(','),
					datasets: [{
						backgroundColor: ['rgba(33, 150, 243, 0.3)'],
						borderColor: ['rgba(33, 150, 243, 1)'],
						data: document.getElementById('upload_count').value.split(','),
						label: 'Uploads',
						// fill: boundary
					}]
				},
				options: Chart.helpers.merge(options, {
					title: {
						// text: 'fill: ' + boundary,
						display: false
					}
				})
			});

		console.log(document.getElementById('download_months').value.split(','));
		new Chart('chart-1', {
				type: 'line',
				data: {
					labels: document.getElementById('download_months').value.split(','),
					datasets: [{
						backgroundColor: ['rgba(33, 150, 243, 0.3)'],
						borderColor: ['rgba(33, 150, 243, 1)'],
						data: document.getElementById('download_count').value.split(','),
						label: 'Downloads',
						// fill: boundary
					}]
				},
				options: Chart.helpers.merge(options, {
					title: {
						// text: 'fill: ' + boundary,
						display: false
					}
				})
			});


		var options = {
			maintainAspectRatio: false,
			spanGaps: false,
			elements: {
				line: {
					tension: 0.000001
				}
			},
			plugins: {
				filler: {
					propagate: false
				}
			},
			scales: {
				xAxes: [{
					ticks: {
						autoSkip: false,
						maxRotation: 0
					}
				}]
			}
		};


