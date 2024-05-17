<?php
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if the username and password are set and not empty
    if (isset($_POST['username']) && isset($_POST['password']) && !empty($_POST['username']) && !empty($_POST['password'])) {
        // Connect to the database (replace placeholders with your actual database credentials)
        $conn = new mysqli("localhost", "netnest", "@Thapelo8427356", "netnest_db");

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Sanitize inputs to prevent SQL injection
        $username = mysqli_real_escape_string($conn, $_POST['username']);
        $password = mysqli_real_escape_string($conn, $_POST['password']);

        // Query to fetch the user from the database
        $sql = "SELECT * FROM users WHERE username = '$username'";
        $result = $conn->query($sql);

        if ($result->num_rows == 1) {
            $row = $result->fetch_assoc();
            // Verify the password using password_verify()
            if (password_verify($password, $row['password'])) {
                // Password is correct, set session variables
                $_SESSION['username'] = $username;
                // Redirect to a logged-in page
                header("Location: dashboard.php");
                exit();
            } else {
                // Incorrect password
                $error = "Invalid username or password.";
            }
        } else {
            // User not found
            $error = "Invalid username or password.";
        }

        // Close connection
        $conn->close();
    } else {
        // Handle missing username or password
        $error = "Username and password are required.";
    }
} else {
    // Redirect to the login page if accessed directly without form submission
    header("Location: login.php");
    exit();
}
?>