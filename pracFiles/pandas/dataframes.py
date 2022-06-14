# this is a very simple pandas file that creates a data frame

# this is to import pandas (obviously)
import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Ugwuegbulam, Chima", "West, Kanye", "Winfrey, Oprah"],
        "Age": [21, 45, 68],
        "Sex": ["M", "M", "F"]
    }
)

print(df)
