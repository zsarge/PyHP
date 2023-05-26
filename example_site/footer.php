{% from datetime import datetime %}

<footer>
    {{ f'&copy; {datetime.now().strftime("%Y")} {author_name}'}}
</footer>