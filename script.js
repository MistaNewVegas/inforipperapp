$(document).ready(function() {
    // Handle form submission with AJAX
    $("#scrapeForm").submit(function(event) {
        event.preventDefault();

        var formData = {
            url: $("#url").val(),
            tag: $("#tag").val()
        };

        // Make sure this matches the endpoint defined in your Flask app for scraping
        $.ajax({
            type: "POST",
            url: "/", 
            data: formData,
            success: function(result) {
                $("#resultContainer").html("<h2>Scraping Result:</h2><p>" + result.result + "</p>");
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });

    // Dark mode toggle script
    $("#darkModeButton").click(function() {
        $("body").toggleClass("dark-mode");
    });

    // Script to use the selected debug info to fill the form
    $("#useDebugInfo").click(function() {
        var selectedIndex = $("#debugInfoSelect").val();
        if (selectedIndex && debugInfo[selectedIndex - 1]) {
            $("#url").val(debugInfo[selectedIndex - 1].url);
            $("#tag").val(debugInfo[selectedIndex - 1].tag);
        }
    });

    // Script to add current form data to debug list
    $("#addToDebugList").click(function() {
        var currentUrl = $("#url").val();
        var currentTag = $("#tag").val();

        if (currentUrl && currentTag) {
            // Make sure this matches the endpoint defined in your Flask app for adding debug info
            $.ajax({
                type: "POST",
                url: "/add_debug_info",
                contentType: "application/json",
                data: JSON.stringify({ url: currentUrl, tag: currentTag }),
                success: function(response) {
                    console.log("Added to debug list:", response);
                    // Optionally update the debugInfoSelect dropdown here
                },
                error: function(error) {
                    console.error("Error adding to debug list:", error);
                }
            });
        }
    });

    // Function to clear the form
    $("#clearFormButton").click(function() {
        $("#url, #tag").val("");
    });
});
