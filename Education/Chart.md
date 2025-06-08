
```dataviewjs
dv.span("📊 Weekly File Creation (Colored by Month)")

const pages = dv.pages('"Education/English Vocabulary"').where(p => p.Created);
const weekCounts = {};
const monthColorMap = {};
const monthPalette = [
	'#4dc9f6', '#f67019', '#f53794', '#537bc4',
	'#acc236', '#166a8f', '#00a950', '#58595b',
	'#8549ba', '#e6194B', '#3cb44b', '#ffe119'
];

let colorIndex = 0;

pages.forEach(p => {
	const date = new Date(p.Created);
	if (isNaN(date)) return;

	const year = date.getFullYear();
	const month = String(date.getMonth() + 1).padStart(2, '0');
	const weekInMonth = Math.ceil(date.getDate() / 7);
	const weekKey = `${year}-${month} (W${weekInMonth})`;

	weekCounts[weekKey] = (weekCounts[weekKey] || 0) + 1;
});

const sortedWeeks = Object.keys(weekCounts).sort((a, b) => {
	const parseKey = k => {
		const [ym, w] = k.split(" (W");
		const [y, m] = ym.split("-");
		const week = parseInt(w);
		return new Date(y, m - 1, week * 7);
	};
	return parseKey(a) - parseKey(b);
});

const counts = sortedWeeks.map(week => weekCounts[week]);

// Get color for each bar based on its month
const backgroundColors = sortedWeeks.map(week => {
	const monthKey = week.slice(0, 7); // 'YYYY-MM'
	if (!monthColorMap[monthKey]) {
		monthColorMap[monthKey] = monthPalette[colorIndex % monthPalette.length];
		colorIndex++;
	}
	return monthColorMap[monthKey];
});

const chartData = {
	type: 'bar',
	data: {
		labels: sortedWeeks,
		datasets: [{
			label: 'Files Created',
			data: counts,
			backgroundColor: backgroundColors,
			borderColor: backgroundColors,
			borderWidth: 1
		}]
	},
	options: {
		scales: {
			y: {
				beginAtZero: true,
				title: {
					display: true,
					text: 'File Count'
				}
			}
		},
		plugins: {
			legend: { display: false },
			tooltip: { enabled: true }
		}
		
	}
};

window.renderChart(chartData, this.container);


```






