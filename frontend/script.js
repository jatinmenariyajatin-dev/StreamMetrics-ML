const API_URL = "http://127.0.0.1:5000/predict";

async function predictRevenue() {

    const data = {
        ucan_members: Number(document.getElementById("ucan_members").value),
        emea_members: Number(document.getElementById("emea_members").value),
        latam_members: Number(document.getElementById("latam_members").value),
        apac_members: Number(document.getElementById("apac_members").value),

        ucan_arpu: Number(document.getElementById("ucan_arpu").value),
        emea_arpu: Number(document.getElementById("emea_arpu").value),
        latam_arpu: Number(document.getElementById("latam_arpu").value),
        apac_arpu: Number(document.getElementById("apac_arpu").value)
    };

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.status === "success") {
            document.getElementById("prediction").innerHTML =
                "Predicted Revenue : $" + result.prediction.toLocaleString();
        } else {
            document.getElementById("prediction").innerHTML =
                result.message;
        }

    } catch (error) {
        document.getElementById("prediction").innerHTML =
            "Unable to connect to Flask Server";
    }
}