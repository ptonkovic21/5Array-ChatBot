async function askQuestion(question) {
	const response = await fetch("http://localhost:8080/ask", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ question }),
	});

	const data = await response.json();
	console.log("5Array: ", data.answer);
}

askQuestion("Who are you?");
