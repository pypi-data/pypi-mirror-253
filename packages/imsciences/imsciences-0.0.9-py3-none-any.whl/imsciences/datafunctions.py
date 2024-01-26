import pandas as pd
import calendar
import plotly.express as px

class dataprocessing:
    
    def remove_rows(self, data_frame, num_rows_to_remove):
        """
        Removes the specified number of rows from the given data frame, including the top row containing column names. 
        The next row will be treated as the new set of column headings.

        Parameters:
        - data_frame: pandas DataFrame
            The input data frame.
        - num_rows_to_remove: int
            The number of rows to remove from the data frame, starting from the original header.

        Returns:
        - pandas DataFrame
            The modified data frame with rows removed and new column headings.

        Raises:
        - TypeError: If num_rows_to_remove is not an integer.
        - ValueError: If num_rows_to_remove is negative or exceeds the total number of rows.
        """
        
        if not isinstance(num_rows_to_remove, int):
            raise TypeError("num_rows_to_remove must be an integer")

        if num_rows_to_remove < 0 or num_rows_to_remove >= len(data_frame):
            raise ValueError("Number of rows to remove must be non-negative and less than the total number of rows in the data frame.")

        if num_rows_to_remove == 0:
            return data_frame

        new_header = data_frame.iloc[num_rows_to_remove - 1]
        modified_data_frame = data_frame[num_rows_to_remove:] 
        modified_data_frame.columns = new_header

        return modified_data_frame
    
    def aggregate_to_wc(self, df, date_column, group_columns, sum_columns, wc):
        """
        Aggregates daily data into weekly data, starting on either Sundays or Mondays as specified, 
        and groups the data by additional specified columns. It sums specified numeric columns, 
        and pivots the data to create separate columns for each combination of the group columns 
        and sum columns. NaN values are replaced with 0 and the index is reset. The day column 
        is renamed from 'Day' to 'OBS'.

        Parameters:
        - df: pandas DataFrame
            The input DataFrame containing daily data.
        - date_column: string
            The name of the column in the DataFrame that contains date information.
        - group_columns: list of strings
            Additional column names to group by along with the weekly grouping.
        - sum_columns: list of strings
            Numeric column names to be summed during aggregation.
        - wc: string
            The week commencing day ('sun' for Sunday or 'mon' for Monday).

        Returns:
        - pandas DataFrame
            A new DataFrame with weekly aggregated data. The index is reset,
            and columns represent the grouped and summed metrics. The DataFrame 
            is in wide format, with separate columns for each combination of 
            grouped metrics.
        """

        # Make a copy of the DataFrame
        df_copy = df.copy()

        # Convert the date column to datetime and set it as the index
        df_copy[date_column] = pd.to_datetime(df_copy[date_column])
        df_copy.set_index(date_column, inplace=True)

        # Convert sum_columns to numeric
        for col in sum_columns:
            df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce').fillna(0).astype(int)

        # Group by week and additional columns, then sum the numeric columns
        if wc == "sun":
            weekly_grouped = df_copy.groupby([pd.Grouper(freq='W-SUN')] + group_columns)[sum_columns].sum()
        elif wc == "mon":
            weekly_grouped = df_copy.groupby([pd.Grouper(freq='W-MON')] + group_columns)[sum_columns].sum()
        else:
            return print("Incorrect week commencing day input. Please choose 'sun' or 'mon'.")

        # Reset index to turn the multi-level index into columns
        weekly_grouped_reset = weekly_grouped.reset_index()

        # Rename 'Day' column to 'OBS' if it exists
        if date_column in weekly_grouped_reset.columns:
            weekly_grouped_reset = weekly_grouped_reset.rename(columns={date_column: 'OBS'})

        # Pivot the data to wide format
        if group_columns:
            wide_df = weekly_grouped_reset.pivot_table(index='OBS', 
                                                    columns=group_columns, 
                                                    values=sum_columns,
                                                    aggfunc='first')
            # Flatten the multi-level column index and create combined column names
            wide_df.columns = [' '.join(col).strip() for col in wide_df.columns.values]
        else:
            wide_df = weekly_grouped_reset.set_index('OBS')

        # Fill NaN values with 0
        wide_df = wide_df.fillna(0)

        # Adding total columns for each unique sum_column
        for col in sum_columns:
            total_column_name = f'Total {col}'
            if group_columns:
                # Columns to sum for each unique sum_column when group_columns is provided
                columns_to_sum = [column for column in wide_df.columns if col in column]
            else:
                # When no group_columns, the column itself is the one to sum
                columns_to_sum = [col]
            wide_df[total_column_name] = wide_df[columns_to_sum].sum(axis=1)

        # Reset the index of the final DataFrame
        wide_df = wide_df.reset_index()

        return wide_df
        
    def convert_monthly_to_daily(self, df, date_column):
        """
        Convert a DataFrame with monthly data to daily data.
        This function takes a DataFrame and a date column, then it expands each
        monthly record into daily records by dividing the numeric values by the number of days in that month.

        :param df: DataFrame with monthly data.
        :param date_column: The name of the column containing the date.
        :return: A new DataFrame with daily data.
        """

        # Convert date_column to datetime
        df[date_column] = pd.to_datetime(df[date_column])

        # Initialize an empty list to hold the daily records
        daily_records = []

        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Calculate the number of days in the month
            num_days = calendar.monthrange(row[date_column].year, row[date_column].month)[1]

            # Create a new record for each day of the month
            for day in range(1, num_days + 1):
                daily_row = row.copy()
                daily_row[date_column] = row[date_column].replace(day=day)

                # Divide each numeric value by the number of days in the month
                for col in df.columns:
                    if pd.api.types.is_numeric_dtype(df[col]) and col != date_column:
                        daily_row[col] = row[col] / num_days

                daily_records.append(daily_row)

        # Convert the list of daily records into a DataFrame
        daily_df = pd.DataFrame(daily_records)
        
        return daily_df
    
    def plot_two(self, df1, col1, df2, col2):
        """
        Plots specified columns from two different dataframes with white background and black axes.

        :param df1: First DataFrame
        :param col1: Column name from the first DataFrame
        :param df2: Second DataFrame
        :param col2: Column name from the second DataFrame
        """

        # Check if columns exist in their respective dataframes
        if col1 not in df1.columns or col2 not in df2.columns:
            raise ValueError("Column not found in respective DataFrame")

        # Rename the columns to ensure they are unique
        col1_new = col1 + ' (df1)'
        col2_new = col2 + ' (df2)' if col1 == col2 else col2

        # Creating a new DataFrame for plotting
        plot_df = pd.DataFrame({
            col1_new: df1[col1],
            col2_new: df2[col2]
        })

        # Plotting using Plotly Express
        fig = px.line(plot_df)

        # Update layout for white background and black axes lines
        fig.update_layout(
            plot_bgcolor='white',
            xaxis=dict(
                showline=True,
                linecolor='black'
            ),
            yaxis=dict(
                showline=True,
                linecolor='black'
            )
        )

        return fig