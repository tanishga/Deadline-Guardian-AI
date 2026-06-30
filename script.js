async function analyseTask() {

    const task = document.getElementById("TaskInput").value;
    const result = document.getElementById("result");

    if (task.trim() === "") {
        result.innerHTML = "⚠️ Please enter a task first.";
        return;
    }

    result.innerHTML = "Gemini is analysing your task...";

    try {

        const response = await fetch("http://127.0.0.1:5000/analyse", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                task: task
            })

        });

        const data = await response.json();

        result.innerHTML = `<pre>${data.response}</pre>`;

    }

    catch (error) {
    console.error(error);
    result.innerHTML = `
        ❌ Error: ${error.message}
    `;
    }

}