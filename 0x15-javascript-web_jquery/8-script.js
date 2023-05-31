const $ = window.$;
$.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
	const res = data.results;
	for (let i = o; i < res.length; i++) {
		$('UL#list_movies').append('<li>' + res[i].title + '</li>');
	}
});
