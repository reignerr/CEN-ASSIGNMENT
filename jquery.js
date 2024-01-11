<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Color-changing Box</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: blue;
    }
  </style>
</head>
<body>
  <div class="box" id="colorBox"></div>

  <script>
    $(document).ready(function(){
      $('#colorBox').click(function(){
        var colors = ['#FF5733', '#33FF57', '#5733FF', '#33FFEC', '#FF33F9'];
        var randomColor = colors[Math.floor(Math.random() * colors.length)];
        $(this).css('background-color', randomColor);
      });
    });
  </script>
</body>
</html>
