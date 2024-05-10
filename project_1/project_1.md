```js
console.log(tankBrown, tankGreen, bulletsBrown, bulletsGreen);
fs.appendFile(
	"data-logs.csv",
	getParams(tankBrown, tankGreen, bulletsBrown, bulletsGreen),
	function (err) {
		if (err) throw err;
		console.log("Saved!");
	}
);
```
