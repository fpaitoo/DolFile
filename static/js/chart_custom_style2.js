/*------------------------------------------------------------------
    File Name: chart_custom_style2.js
    Template Name: Pluto - Responsive HTML5 Template
    Created By: dashboard.design
    Envato Profile: https://themeforest.net/user/htmldotdesign
    Website: https://html.design
    Version: 1.0
-------------------------------------------------------------------*/

var presets = window.chartColors;
		var utils = Samples.utils;
		var inputs = {
			min: -50,
			max: 50,
			count: 10,
			decimals: 2,
			continuity: 1
		};

		function generateData(config) {
			return utils.numbers(Chart.helpers.merge(inputs, config || {}));
		}


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


		function generateLabels(config) {
			return utils.months(Chart.helpers.merge({
				count: inputs.count,
				section: 3
			}, config || {}));
		}

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

		[false, 'origin', 'start', 'end'].forEach(function(boundary, index) {

			// reset the random seed to generate the same data for all charts
			utils.srand(8);

			new Chart('chart-' + index1, {
				type: 'line',
				data: {
					labels: generateLabels(),
					datasets: [{
						backgroundColor: ['rgba(33, 150, 243, 0.3)'],
						borderColor: ['rgba(33, 150, 243, 1)'],	
						data: generateData(),
						label: 'Progress chart',
						fill: boundary
					}]
				},
				options: Chart.helpers.merge(options, {
					title: {
						text: 'fill: ' + boundary,
						display: false
					}
				})
			});
		});

		// eslint-disable-next-line no-unused-vars
		function toggleSmooth(btn) {
			var value = btn.classList.toggle('btn-on');
			Chart.helpers.each(Chart.instances, function(chart) {
				chart.options.elements.line.tension = value ? 0.4 : 0.000001;
				chart.update();
			});
		}

		// eslint-disable-next-line no-unused-vars
		function randomize() {
			var seed = utils.rand();
			Chart.helpers.each(Chart.instances, function(chart) {
				utils.srand(seed);

				chart.data.datasets.forEach(function(dataset) {
					dataset.data = generateData();
				});

				chart.update();
			});
		}