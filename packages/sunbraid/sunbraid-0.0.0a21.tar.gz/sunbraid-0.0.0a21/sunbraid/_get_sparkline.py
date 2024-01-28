def get_sparkline_import():
    import requests
    sparkline_code = requests.get("https://omnipotent.net/jquery.sparkline/2.1.2/jquery.sparkline.js").text

    func = """
    $(function() {
        /** This code runs when everything has been loaded on the page */
        /* Inline sparklines take their values from the contents of the tag */
        $('.inlinesparkline').sparkline(); 
    
        /* Sparklines can also take their values from the first argument 
        passed to the sparkline() function */
        var myvalues = [10,8,5,7,4,4,1];
        $('.dynamicsparkline').sparkline(myvalues);
    
        /* The second argument gives options such as chart type */
        $('.dynamicbar').sparkline(myvalues, {type: 'bar', barColor: 'green'} );
    
        /* Use 'html' instead of an array of values to pass options 
        to a sparkline with data in the tag */
        $('.inlinebar').sparkline('html', {type: 'bar', barColor: 'red'} );
    });
    """

    return f"""
        <script src="https://code.jquery.com/jquery-1.7.2.min.js"></script>
        <script> {sparkline_code} </script>
        <script type="text/javascript"> {func} </script>
        """