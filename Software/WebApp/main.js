window.addEventListener("load", () => {
	send_button = document.getElementById("send_button");

	send_button.addEventListener("click", () => {
		question_element = document.getElementById("question");
		question = question_element.value;

		question_element = "";

		chatBox.innerHTML += `<span class="you">You:</span> ${question}<br>`;

		ask(question);
	});
});

async function ask(question) {
	if (!question) return;

	let chatBox = document.getElementById("chat");

	thinking =
		chatBox.innerHTML += `<span class="bot">5Array is thinking...</span><br>`;

	try {
		const res = await fetch("http://localhost:8080/ask", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ question }),
		});
		const data = await res.json();

		chatBox.innerHTML = chatBox.innerHTML.replace(
			thinking,
			`<span class="bot">5Array:</span> ${data.answer}<br>`
		);
	} catch (err) {
		chatBox.innerHTML += `<span class="bot">Error:</span> ${err.message}<br>`;
	}
}
