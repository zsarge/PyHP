<!DOCTYPE html>
<html lang="en">

{{ include('./head.php') }}
{% author_name = "Zack Sargent" # used in the footer %}

<body>
    <h1> Hello World! </h1>
    {% import time %}
    <p>
        Generated at {{ time.time() }}
    </p>

    {{ include('./footer.php') }}
</body>

</html>