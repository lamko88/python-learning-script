
import osu_apis


def main():
    # Creating an object to an OSU API class
    api_class_obj = osu_apis.osu_api_class()

    """Get user's config data

    :param client_id: user's client_id
    :param client_secret: user's client_secret
    :param grant_type: hard-coded value, client_credentials
    :param host: host url
    """
    config_dict = api_class_obj.read_config()

    # Get access_token using user's config.json data
    access_token = api_class_obj.get_access_token(
                        config_dict['client_id'],
                        config_dict['client_secret'],
                        config_dict['host_url']
                    )

    # Get header data using access_token value
    headers = api_class_obj.get_headers(access_token)

    """User's query data inputs

    :param onid: user's onid choice for query
    :type: string
    :param building_abbr: user's building abbreviated choice for query
    :type: string
    :param calendar_year: user's calendar year choice for query
    :type: string
    """
    while True:
        try:
            onid = str(input('\nEnter ONID name: '))
            building_abbr = str(input('Enter Building Abbr(Ex: JSB): '))
            calendar_year = str(input('Enter Calendar Year(Example: 2022): '))
        except ValueError:
            print('\nInvalid data type or Missing data. ' +
                  'Please try again...\n')
            continue
        if not (
                onid.isalpha() and building_abbr.isalpha() and
                calendar_year.isdigit()
               ):
            print('\nOops, invalid data type. ' +
                  'Please try entering the data again...\n')
        else:
            break

    params = {
          'filter[onid]': onid,
          'q': building_abbr,
          'calendarYear': calendar_year,
    }

    # Get directory response data using user's data inputs
    print(
        '\nResponse Data for Directory:\n',
        api_class_obj.get_response(
            config_dict['host_url'],
            config_dict['directory_url'],
            headers=headers,
            params=params
        )
    )

    # Get location response data using user's data inputs
    print(
        '\nResponse Data for Location:\n',
        api_class_obj.get_response(
            config_dict['host_url'],
            config_dict['location_url'],
            headers=headers,
            params=params
        )
    )

    # Get terms response data using user's data inputs
    print(
        '\nResponse Data for Terms:\n',
        api_class_obj.get_response(
            config_dict['host_url'],
            config_dict['terms_url'],
            headers=headers,
            params=params
        )
    )


if __name__ == '__main__':
    main()
