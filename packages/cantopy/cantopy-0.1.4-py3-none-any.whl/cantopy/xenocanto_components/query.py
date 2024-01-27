# Additional information on the Xeno Canto API can be found at:
# https://www.xeno-canto.org/explore/api


class Query:
    """Wrapper for a query passed to the Xeno Canto API.

    Attributes
    ----------
    species_name : str
        The name of the species, can be either the English name, the scientific name, or the scientific name of the family.
    group : str
        The group of the recording (e.g., 'birds', 'grasshoppers', 'bats').
    genus : str
        The genus name of the species.
    subspecies : str
        The subspecies.
    recordist_id : str
        The id of the person who uploaded the recording.
    country : str
        The country of the recording.
    location : str
        The location of the recording.
    remarks : str
        Additional remarks for the recording.
    animal_seen : str
        If the animal was seen.
    playback_used : str
        The playback used attribute to set.
    latitude : str
        The latitude of the recording.
    longitude : str
        The longitude of the recording.
    coordinate_box : str
        The coordinate box which should contain the recording location.
    also_attribute : str
        The 'also' attribute is used to search for background species in a recording.
    song_type : str
        The type of song in the recording.
    other_type : str
        The 'other type' attribute is used when the type field does not contain the desired sound type.
    sex : str
        The sex of the species.
    life_stage : str
        The life stage attribute to set, valid values are: "adult", "juvenile", "nestling", "nymph", and "subadult".
    recording_method : str
        The recording method of the recording.
    catalog_number : str
        The catalog number of recording to search for a specific recording.
    recording_license : str
        The recording license.
    quality : str
        The quality of the recording.
    recording_length : str
        The length of the recording.
    world_area : str
        The general world area of the recording.
    uploaded_since : str
        Search for recordings UPLOADED after a certain date.
    recorded_year : str
        Search for recordings RECORDED in a certain year.
    recorded_month : str
        Search for recordings RECORDED in a certain month.
    sample_rate : str
        The sample rate of the recording.
    """

    def __init__(
        self,
        species_name: str,
        group: str = "None",
        genus: str = "None",
        subspecies: str = "None",
        recordist_id: str = "None",
        country: str = "None",
        location: str = "None",
        remarks: str = "None",
        animal_seen: str = "None",
        playback_used: str = "None",
        latitude: str = "None",
        longitude: str = "None",
        coordinate_box: str = "None",
        also_attribute: str = "None",
        song_type: str = "None",
        other_type: str = "None",
        sex: str = "None",
        life_stage: str = "None",
        recording_method: str = "None",
        catalog_number: str = "None",
        recording_license: str = "None",
        quality: str = "None",
        recording_length: str = "None",
        world_area: str = "None",
        uploaded_since: str = "None",
        recorded_year: str = "None",
        recorded_month: str = "None",
        sample_rate: str = "None",
    ):
        """Initialize the query object for passing to the Xeno Canto API.

        Parameters
        ----------
        species_name : str
            The name to set, can be either the English name, the scientific name, or the scientific name of the family.
        group : str, optional
            The group to set, valid values are: 'birds', 'grasshoppers', or 'bats'.
            This can also be set using their respective ids: '1', '2', and '3'. Recordings may include multiple groups,
            use 'soundscape' or '0' to include all groups.
        genus : str, optional
            The genus name to set, field uses a 'starts with' rather than 'contains' query and accepts a 'matches' operator.
        subspecies : str, optional
            The subspecies to set, field uses a 'starts with' rather than 'contains' query and accepts a 'matches' operator.
        recordist_id : str, optional
            The recordist to set, field accepts a 'matches' operator.
        country : str, optional
            The country to set, field uses a 'starts with' query and accepts a 'matches' operator.
        location : str, optional
            The location to set, field accepts a 'matches' operator.
        remarks : str, optional
            The remarks to set, field accepts a 'matches' operator.
        animal_seen : str, optional
            The animal seen attribute to set.
        playback_used : str, optional
            The playback used attribute to set.
        latitude : str, optional
            The latitude to set, used in conjunction with the lon field to search within one degree of a location.
            This field also accepts '<' and '>' operators.
        longitude : str, optional
            The longitude to set, used in conjunction with the lat field to search within one degree of a location.
            This field also accepts '<' and '>' operators.
        coordinate_box : str, optional
            The coordinate box to set, this box is formatted as follows: LAT_MIN,LON_MIN,LAT_MAX,LON_MAX.
            This field also accepts '<' and '>' operators.
        also_attribute : str, optional
            The also attribute to set, the also attribute is used to search for background species in a recording.
        song_type : str, optional
            The type attribute to set, valid values for this tag are: "aberrant", "alarm call", "begging call", "call",
            "calling song", "courtship song", "dawn song", "distress call", "disturbance song", "drumming", "duet",
            "echolocation", "female song", "flight call", "flight song", "imitation", "nocturnal flight call",
            "rivalry song", "searching song", "social call", "song", "subsong". This field always uses a 'matches' operator.
        other_type : str, optional
            The other type attribute to set, this field is used when the type field does not contain the desired sound type
            e.g., "wing flapping".
        sex : str, optional
            The sex attribute to set, valid values are: "male" and "female". This field always uses a 'matches' operator.
        life_stage : str, optional
            The life stage attribute to set, valid values are: "adult", "juvenile", "nestling", "nymph", and "subadult".
            This field always uses a 'matches' operator.
        recording_method : str, optional
            The recording method attribute to set, valid values are: "emerging from roost", "field recording",
            "fluorescent light tag", "hand-release", "in enclosure", "in net", "in the hand", "roosting", "roped",
            "studio recording". This field always uses a 'matches' operator.
        catalog_number : str, optional
            The catalog number of recordings attribute to set, this field is used to search for a specific recording.
            It can also be used to search for a range of recordings e.g. 1-10.
        recording_license : str, optional
            The recording license attribute to set, valid values are: "BY" (Attribution), "NC" (NonCommercial), "SA"
            (ShareAlike), "ND" (NoDerivatives), "CC0" (Public Domain/copyright-free) and "PD" (no restrictions (=BY-NC-SA)).
            Conditions can be combined e.g. "BY-NC-SA". This field always uses a 'matches' operator.
        quality : str, optional
            The quality attribute to set, valid values range from "A" (best) to "E" (worst). This field accepts "<" and ">" operators.
        recording_length : str, optional
            The recording length attribute to set, this field accepts "<", ">" and "=" operators.
        world_area : str, optional
            The area attribute to set, valid values are: "africa", "america", "asia", "australia", "europe".
        uploaded_since : str, optional
            The since attribute to set, this field is used to search for recordings UPLOADED after a certain date,
            date format is YYYY-MM-DD.
        recorded_year : str, optional
            The year attribute to set, this field is used to search for recordings RECORDED in a certain year,
            date format is YYYY, this field accepts "<" and ">" operators.
        recorded_month : str, optional
            The month attribute to set, this field is used to search for recordings RECORDED in a certain month,
            date format is MM, this field accepts "<" and ">" operators.
        sample_rate : str, optional
            The sample rate attribute to set, this field accepts "<" and ">" operators.
        """

        self.species_name = species_name
        self.group = group
        self.genus = genus
        self.subspecies = subspecies
        self.recordist_id = recordist_id
        self.country = country
        self.location = location
        self.remarks = remarks
        self.animal_seen = animal_seen
        self.playback_used = playback_used
        self.latitude = latitude
        self.longitude = longitude
        self.coordinate_box = coordinate_box
        self.also_attribute = also_attribute
        self.song_type = song_type
        self.other_type = other_type
        self.sex = sex
        self.life_stage = life_stage
        self.recording_method = recording_method
        self.catalog_number = catalog_number
        self.recording_license = recording_license
        self.quality = quality
        self.recording_length = recording_length
        self.world_area = world_area
        self.uploaded_since = uploaded_since
        self.recorded_year = recorded_year
        self.recorded_month = recorded_month
        self.sample_rate = sample_rate

    def to_string(self) -> str:
        """Generate a string representation of the XenoCantoQuery object for passing to the Xeno Canto API.

        Returns
        -------
        str
            The string representation of the XenoCantoQuery object.
        """

        attributes = [
            f"{self.species_name}",
            f'group:"{self.group}"',
            f'gen:"{self.genus}"',
            f'ssp:"{self.subspecies}"',
            f'rec:"{self.recordist_id}"',
            f'cnt:"{self.country}"',
            f'loc:"{self.location}"',
            f'rmk:"{self.remarks}"',
            f'seen:"{self.animal_seen}"',
            f'playback:"{self.playback_used}"',
            f'lat:"{self.latitude}"',
            f'lon:"{self.longitude}"',
            f'box:"{self.coordinate_box}"',
            f'also:"{self.also_attribute}"',
            f'type:"{self.song_type}"',
            f'othertype:"{self.other_type}"',
            f'sex:"{self.sex}"',
            f'stage:"{self.life_stage}"',
            f'method:"{self.recording_method}"',
            f'nr:"{self.catalog_number}"',
            f'license:"{self.recording_license}"',
            f'q:"{self.quality}"',
            f'length:"{self.recording_length}"',
            f'area:"{self.world_area}"',
            f'since:"{self.uploaded_since}"',
            f'year:"{self.recorded_year}"',
            f'month:"{self.recorded_month}"',
            f'smp:"{self.sample_rate}"',
        ]

        # Remove the None values
        attributes = [attribute for attribute in attributes if "None" not in attribute]

        return "+".join(filter(None, attributes))
