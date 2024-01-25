"""Streamlit-based web interface for ProteoBench."""

import json
import logging
import uuid
from datetime import datetime

import streamlit as st
import streamlit_utils
from streamlit_extras.let_it_rain import rain

from proteobench.modules.dda_quant.datapoint import (
    filter_df_numquant_median_abs_epsilon,
    filter_df_numquant_nr_prec,
)
from proteobench.modules.dda_quant.module import Module
from proteobench.modules.dda_quant.parse_settings import (
    INPUT_FORMATS,
    LOCAL_DEVELOPMENT,
    ParseSettings,
)
from proteobench.modules.dda_quant.plot import PlotDataPoint

logger = logging.getLogger(__name__)

ALL_DATAPOINTS = "all_datapoints"
SUBMIT = "submit"
FIG1 = "fig1"
FIG2 = "fig2"
RESULT_PERF = "result_perf"
META_DATA = "meta_data"
INPUT_DF = "input_df"
META_FILE_UPLOADER_UUID = "meta_file_uploader_uuid"
COMMENTS_SUBMISSION_UUID = "comments_submission_uuid"
CHECK_SUBMISSION_UUID = "check_submission_uuid"
BUTTON_SUBMISSION_UUID = "button_submission_uuid"

DEFAULT_VAL_SLIDER = 3

if "submission_ready" not in st.session_state:
    st.session_state["submission_ready"] = False


class StreamlitUI:
    """Proteobench Streamlit UI."""

    def __init__(self):
        """Proteobench Streamlit UI."""
        self.texts = WebpageTexts
        self.user_input = dict()

        st.set_page_config(
            page_title="Proteobench web server",
            page_icon=":rocket:",
            layout="wide",
            initial_sidebar_state="expanded",
        )
        if SUBMIT not in st.session_state:
            st.session_state[SUBMIT] = False
        self._main_page()
        self._sidebar()

    def generate_input_field(self, input_format: str, content: dict):
        if content["type"] == "text_input":
            if "placeholder" in content:
                return st.text_input(content["label"], placeholder=content["placeholder"])
            elif "value" in content:
                return st.text_input(content["label"], content["value"][input_format])
        if content["type"] == "number_input":
            return st.number_input(
                content["label"],
                value=None,
                format=content["format"],
                min_value=content["min_value"],
                max_value=content["max_value"],
            )
        if content["type"] == "selectbox":
            return st.selectbox(
                content["label"],
                content["options"],
                content["options"].index(content["value"][input_format]),
            )
        if content["type"] == "checkbox":
            return st.checkbox(content["label"], content["value"][input_format])

    def _main_page(self):
        """Format main page."""
        st.title("DDA quantification - precursor ions")
        st.warning(
            "This module is in BETA phase. The figure presented below and the metrics calculation may change in the near future."
        )
        st.header("Description of the module")
        st.markdown(
            """
                    This module compares the MS1-level quantification tools for
                    data-dependent acquisition (DDA). The raw files provided for
                    this module are presented in the comprehensive LFQ benchmark
                    dataset from [Van Puyvelde et al., 2022](https://www.nature.com/articles/s41597-022-01216-6).
                    The samples contain tryptic peptides from Homo sapiens,
                    Saccharomyces cerevisiae, and Escherichia coli, mixed in different
                    ratios (condition A and condition B), with three replicates of each
                    condition. With these samples, we calculate three metrics:
                    - To estimate the sensitivity of the workflows, we report the
                    number of unique precursors (charged modified sequence) quantified
                    in all 6 runs.
                    - To estimate the accuracy of the workflows, we report the weighted
                    sum of precursor deviation from expected ratios.
                    - To estimate the precision of the workflows, we report the weighted
                     average of the interquartile range (IQR) of the precursors ratio.

                    ProteoBench plots these three metrics to visualize workflow outputs
                     from different tools, with different versions, and/or different
                    sets of parameters for the search and quantification.
                    The full description of the pre-processing steps and metrics
                    calculation is available [here](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/).
                    """
        )
        st.header("Downloading associated files")
        st.markdown(
            """
                    The raw files used for this module were acquired on an Orbitrap
                    Q-Exactive H-FX (ThermoScientific). They can be downloaded from the
                    proteomeXchange repository PXD028735. You can download them here:

                    [LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_01.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_01.raw),
                    [LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_02.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_02.raw),
                    [LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_03.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_A_Sample_Alpha_03.raw),
                    [LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_01.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_01.raw),
                    [LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_02.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_02.raw),
                    [LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_03.raw](https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD028735/LFQ_Orbitrap_DDA_Condition_B_Sample_Alpha_03.raw)

                    **It is imperative not to rename the files once downloaded!**
                    """
        )
        st.markdown(
            """
                    Download the zipped FASTA file here: <a href="/app/static/ProteoBenchFASTA_DDAQuantification.zip" download>ProteoBenchFASTA_DDAQuantification.zip</a>.
                    The fasta file provided for this module contains the three species
                    present in the samples and contaminant proteins
                    ([Frankenfield et al., JPR](https://pubs.acs.org/doi/10.1021/acs.jproteome.2c00145))
                    """,
            unsafe_allow_html=True
        )

        st.header("Input and configuration")

        st.markdown(
            """
                   Scroll down if you want to see the public benchmark runs publicly available
                   today.
                    """
        )

        with st.form(key="main_form"):
            st.subheader("Input files")
            st.markdown(
                """
                    Please upload the ouput of your analysis, and indicate what software 
                    tool it comes from (this is necessary to correctly parse your table - find 
                    more information in the "[How to use](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/)" 
                    section of this module).

                    Remember: contaminant sequences are already present in the fasta file 
                    associated to this module. **Do not add other contaminants** to your 
                    search. This is important when using MaxQuant and FragPipe, among other tools.
                    """
            )
            self.user_input["input_csv"] = st.file_uploader(
                "Software tool result file", help=self.texts.Help.input_file
            )

            self.user_input["input_format"] = st.selectbox(
                "Software tool", INPUT_FORMATS, help=self.texts.Help.input_format
            )

            # self.user_input["pull_req"] = st.text_input(
            #     "Open pull request to make results available to everyone (type \"YES\" to enable)",
            #     "NO"
            # )
            st.markdown(
                """
                    Additionally, you can fill out some information on the paramters that 
                    were used for this benchmark run bellow. These will be printed when 
                    hovering on your point.
                    """
            )
            with st.expander("Additional parameters"):
                with open("../webinterface/configuration/dda_quant.json") as file:
                    config = json.load(file)

                for key, value in config.items():
                    self.user_input[key] = self.generate_input_field(self.user_input["input_format"], value)

            st.markdown(
                """
                    Now, press `Parse and Bench` to calculate the metrics from your input. 
                    """
            )

            submit_button = st.form_submit_button("Parse and bench", help=self.texts.Help.parse_button)

        # if st.session_state[SUBMIT]:
        if FIG1 in st.session_state:
            self._populate_results()

        if "slider_id" in st.session_state.keys():
            default_val_slider = st.session_state[st.session_state["slider_id"]]
        else:
            default_val_slider = DEFAULT_VAL_SLIDER

        if ALL_DATAPOINTS not in st.session_state:
            st.session_state[ALL_DATAPOINTS] = None
            all_datapoints = st.session_state[ALL_DATAPOINTS]
            all_datapoints = Module().obtain_all_data_point(all_datapoints)

            all_datapoints["median_abs_epsilon"] = all_datapoints["results"].apply(
                filter_df_numquant_median_abs_epsilon, min_quant=default_val_slider
            )
            all_datapoints["nr_prec"] = all_datapoints["results"].apply(
                filter_df_numquant_nr_prec, min_quant=default_val_slider
            )

            fig2 = PlotDataPoint().plot_metric(all_datapoints)

            st.session_state[ALL_DATAPOINTS] = all_datapoints
            st.session_state[FIG2] = fig2

        st.session_state["slider_id"] = uuid.uuid4()
        st.markdown(
            """
                Choose with the slider below the minimum number of quantification value 
                per raw file.  
                Example: when 3 is selected, only the precursor ions quantified in 
                3 or more raw files will be considered for the plot. 
                    """
        )

        f = st.select_slider(
            label="Minimal ion quantifications (# samples)",
            options=[1, 2, 3, 4, 5, 6],
            value=default_val_slider,
            on_change=self.slider_callback,
            key=st.session_state["slider_id"],
        )

        st.plotly_chart(st.session_state[FIG2], use_container_width=True)

        if submit_button:
            if self.user_input["input_csv"]:
                if META_FILE_UPLOADER_UUID in st.session_state.keys():
                    del st.session_state[META_FILE_UPLOADER_UUID]
                if COMMENTS_SUBMISSION_UUID in st.session_state.keys():
                    del st.session_state[COMMENTS_SUBMISSION_UUID]
                if CHECK_SUBMISSION_UUID in st.session_state.keys():
                    del st.session_state[CHECK_SUBMISSION_UUID]
                if BUTTON_SUBMISSION_UUID in st.session_state.keys():
                    del st.session_state[BUTTON_SUBMISSION_UUID]

                self._run_proteobench()
            else:
                error_message = st.error(":x: Please provide a result file")

    def _populate_results(self):
        self.generate_results("", None, None, False, None)

    def _sidebar(self):
        """Format sidebar."""
        st.sidebar.image("logos/logo_funding/main_logos_sidebar.png", width=300)

        # st.sidebar.markdown(self.texts.Sidebar.badges)
        st.sidebar.header("About")
        st.sidebar.markdown(self.texts.Sidebar.about, unsafe_allow_html=True)

    def _run_proteobench(self):
        # Run Proteobench
        st.header("Running Proteobench")
        status_placeholder = st.empty()
        status_placeholder.info(":hourglass_flowing_sand: Running Proteobench...")

        if ALL_DATAPOINTS not in st.session_state:
            st.session_state[ALL_DATAPOINTS] = None

        try:
            if "slider_id" in st.session_state.keys():
                default_val_slider = st.session_state[st.session_state["slider_id"]]
            else:
                default_val_slider = DEFAULT_VAL_SLIDER
            result_performance, all_datapoints, input_df = Module().benchmarking(
                self.user_input["input_csv"],
                self.user_input["input_format"],
                self.user_input,
                st.session_state[ALL_DATAPOINTS],
                default_cutoff_min_prec=default_val_slider,
            )
            st.session_state[ALL_DATAPOINTS] = all_datapoints
        except Exception as e:
            status_placeholder.error(":x: Proteobench ran into a problem")
            st.exception(e)
        else:
            self.generate_results(status_placeholder, result_performance, all_datapoints, True, input_df)

    def slider_callback(self):
        min_quant = st.session_state[st.session_state["slider_id"]]
        st.session_state[ALL_DATAPOINTS]["median_abs_epsilon"] = [
            filter_df_numquant_median_abs_epsilon(v, min_quant=min_quant)
            for v in st.session_state[ALL_DATAPOINTS]["results"]
        ]
        st.session_state[ALL_DATAPOINTS]["nr_prec"] = [
            filter_df_numquant_nr_prec(v, min_quant=min_quant) for v in st.session_state[ALL_DATAPOINTS]["results"]
        ]

        fig2 = PlotDataPoint().plot_metric(st.session_state[ALL_DATAPOINTS])

        st.session_state[FIG2] = fig2
        st.session_state[FIG2].data[0].x = fig2.data[0].x
        st.session_state[FIG2].data[0].y = fig2.data[0].y

    def generate_results(
        self,
        status_placeholder,
        result_performance,
        all_datapoints,
        recalculate,
        input_df,
    ):
        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if recalculate:
            status_placeholder.success(":heavy_check_mark: Finished!")

            # Show head of result DataFrame
        st.header("Results")
        st.subheader("Sample of the processed file")
        st.markdown(
            """
                   Here are the data from your benchmark run. The table contains the 
                   precursor ion MS signal calculated from your input data. You can download 
                   this table from `Download calculated ratios` below.
                    """
        )
        if not recalculate:
            result_performance = st.session_state[RESULT_PERF]
            all_datapoints = st.session_state[ALL_DATAPOINTS]
            input_df = st.session_state[INPUT_DF]
        st.dataframe(result_performance.head(100))
        st.markdown(
            """
                   It contains the following columns:

                   - precursor ion = concatenation of the modified sequence en charge
                   - mean log2-transformed intensities for condition A and B
                   - standard deviations calculated for the log2-transformed values in condition A and B
                   - mean intensity for condition A and B
                   - standard deviations calculated for the intensity values in condition A and B
                   - coefficient of variation (CV) for condition A and B
                   - differences of the mean log2-transformed values between condition A and B
                   - MS signal from the input table ("abundance_DDA_Condition_A_Sample_Alpha_01" to "abundance_DDA_Condition_B_Sample_Alpha_03")
                   - Count = number of runs with non-missing values
                   - species the sequence matches to
                   - unique = TRUE if the sequence is species-specific
                   - species
                   - expected ratio for the given species
                   - epsilon = difference of the observed and expected log2-transformed fold change
                    """
        )
        # Plot results
        st.subheader("Ratio between conditions")
        st.markdown(
            """
                   Ratios calculated from your data:
                    """
        )
        if recalculate:
            parse_settings = ParseSettings(self.user_input["input_format"])
            fig = PlotDataPoint().plot_fold_change_histogram(result_performance, parse_settings.species_expected_ratio)
        else:
            fig = st.session_state[FIG1]
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Mean error between conditions")
        st.markdown(
            """
                   New figure including your benchmark run. The point corresponding to 
                   your data will appear bigger than the public data sets already available 
                   in ProteoBench.
                    """
        )
        # show metadata
        # st.text(all_datapoints.head(100))

        if "slider_id" in st.session_state.keys():
            default_val_slider = st.session_state[st.session_state["slider_id"]]
        else:
            default_val_slider = DEFAULT_VAL_SLIDER

        if recalculate:
            all_datapoints["weighted_sum"] = [
                filter_df_numquant_median_abs_epsilon(v, min_quant=default_val_slider)
                for v in all_datapoints["results"]
            ]
            all_datapoints["nr_prec"] = [
                filter_df_numquant_nr_prec(v, min_quant=default_val_slider) for v in all_datapoints["results"]
            ]

            fig2 = PlotDataPoint().plot_metric(all_datapoints)
        else:
            fig2 = st.session_state[FIG2]

        st.session_state["slider_id"] = uuid.uuid4()
        st.markdown(
            """
                   Choose with the slider below the minimum number of quantification value 
                   per raw file.  
                   Example: when 3 is selected, only the precursor ions quantified in 
                   3 or more raw files will be considered for the plot. 
                    """
        )

        f = st.select_slider(
            label="Minimal ion quantifications (# samples)",
            options=[1, 2, 3, 4, 5, 6],
            value=default_val_slider,
            on_change=self.slider_callback,
            key=st.session_state["slider_id"],
        )

        st.plotly_chart(fig2, use_container_width=True)

        sample_name = "%s-%s-%s-%s" % (
            self.user_input["input_format"],
            self.user_input["software_version"],
            self.user_input["enable_match_between_runs"],
            time_stamp,
        )

        # Download link
        st.subheader("Download calculated ratios")
        random_uuid = uuid.uuid4()
        st.download_button(
            label="Download",
            data=streamlit_utils.save_dataframe(result_performance),
            file_name=f"{sample_name}.csv",
            mime="text/csv",
            key=f"{random_uuid}",
        )

        st.subheader("Add results to online repository")
        st.markdown(
            """
                    **Please make these results available to the entire community!**

                    To do so, you need to provide the parameter file that corresponds to 
                    your analysis. You can upload it in the drag and drop area below. 
                    See [here](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/)
                    for all compatible parameter files.
                    In this module, we keep track of the following parameters, if you feel 
                    that some important information is missing, please add it in the 
                    `Comments for submission` field. 
                    - software tool name and version
                    - search engine name and version
                    - FDR threshold for PSM, peptide and protein level
                    - match between run (or not)
                    - precursor mass tolerance
                    - enzyme (although for these data it should be Trypsin)
                    - number of missed-cleavages
                    - minimum and maximum peptide length
                    - fixed and variable modifications
                    - maximum number of modifications
                    - minimum and maximum precursor charge

                    Once you confirm that the metadata is correct (and corresponds to the 
                    table you uploaded before generating the plot), a button will appear.
                    Press it to submit. 

                    Once submitted, you will see a weblink that will prompt you to a 
                    pull request on the github repository of the module. Please write down
                    its number to keep track of your submission. If it looks good, one of 
                    us will accept it and make your data public. 

                    Please contact us if you have any issue. To do so, you can create an 
                    [issue](https://github.com/Proteobench/ProteoBench/issues/new) on our 
                    github, or send us an email [TODO].
                    """
        )
        st.session_state[FIG1] = fig
        st.session_state[FIG2] = fig2
        st.session_state[RESULT_PERF] = result_performance
        st.session_state[ALL_DATAPOINTS] = all_datapoints
        st.session_state[INPUT_DF] = input_df

        # Create unique element IDs
        if META_FILE_UPLOADER_UUID in st.session_state.keys():
            meta_file_uploader_uuid = st.session_state[META_FILE_UPLOADER_UUID]
        else:
            meta_file_uploader_uuid = uuid.uuid4()
            st.session_state[META_FILE_UPLOADER_UUID] = meta_file_uploader_uuid
        if COMMENTS_SUBMISSION_UUID in st.session_state.keys():
            comments_submission_uuid = st.session_state[COMMENTS_SUBMISSION_UUID]
        else:
            comments_submission_uuid = uuid.uuid4()
            st.session_state[COMMENTS_SUBMISSION_UUID] = comments_submission_uuid
        if CHECK_SUBMISSION_UUID in st.session_state.keys():
            check_submission_uuid = st.session_state[CHECK_SUBMISSION_UUID]
        else:
            check_submission_uuid = uuid.uuid4()
            st.session_state[CHECK_SUBMISSION_UUID] = check_submission_uuid

        self.user_input[META_DATA] = st.file_uploader(
            "Meta data for searches",
            help=self.texts.Help.meta_data_file,
            key=meta_file_uploader_uuid,
        )

        self.user_input["comments_for_submission"] = st.text_area(
            "Comments for submission",
            placeholder="Anything else you want to let us know? Please specifically add changes in your search parameters here, that are not obvious from the parameter file.",
            height=200,
            key=comments_submission_uuid,
        )

        checkbox = st.checkbox(
            "I confirm that the metadata is correct",
            key=check_submission_uuid,
        )

        # TODO: do we need a better handling of this?
        params = None
        if self.user_input[META_DATA]:
            try:
                params = Module().load_params_file(self.user_input[META_DATA], self.user_input["input_format"])
            except KeyError as e:
                st.error("Parsing of meta parameters file for this software is not supported yet.")
            except Exception as err:
                input_f = self.user_input["input_format"]
                st.error(
                    f"Unexpected error while parsing file. Make sure you privded a meta parameters file produced by {input_f}."
                )

        if checkbox and params != None:
            st.session_state["submission_ready"] = True

            if BUTTON_SUBMISSION_UUID in st.session_state.keys():
                button_submission_uuid = st.session_state[BUTTON_SUBMISSION_UUID]
            else:
                button_submission_uuid = uuid.uuid4()
                st.session_state[BUTTON_SUBMISSION_UUID] = button_submission_uuid
            submit_pr = st.button("I really want to upload it", key=button_submission_uuid)

            # submit_pr = False
            if submit_pr:
                st.session_state[SUBMIT] = True
                user_comments = self.user_input["comments_for_submission"]
                if not LOCAL_DEVELOPMENT:
                    pr_url = Module().clone_pr(
                        st.session_state[ALL_DATAPOINTS],
                        params,
                        st.secrets["gh"]["token"],
                        username="Proteobot",
                        remote_git="github.com/Proteobot/Results_Module2_quant_DDA.git",
                        branch_name="new_branch",
                        submission_comments=user_comments,
                    )
                else:
                    DDA_QUANT_RESULTS_PATH = Module().write_json_local_development(
                        st.session_state[ALL_DATAPOINTS], params
                    )

                id = str(all_datapoints[all_datapoints["old_new"] == "new"].iloc[-1, :]["intermediate_hash"])

                if "storage" in st.secrets.keys():
                    Module().write_intermediate_raw(
                        st.secrets["storage"]["dir"],
                        id,
                        input_df,
                        result_performance,
                        self.user_input[META_DATA],
                    )
        if SUBMIT in st.session_state:
            if st.session_state[SUBMIT]:
                # status_placeholder.success(":heavy_check_mark: Successfully uploaded data!")
                st.subheader("SUCCESS")
                st.markdown(
                    """
                    **It will take a few working days for your point to be added to the plot**
                    """
                )
                try:
                    st.write(f"Follow your submission approval here: [{pr_url}]({pr_url})")
                except UnboundLocalError:
                    # Happens when pr_url is not defined, e.g., local dev
                    pass
                

                st.session_state[SUBMIT] = False
                rain(emoji="🎈", font_size=54, falling_speed=5, animation_length=1)


class WebpageTexts:
    class Sidebar:
        about = f"""
            """

    class Help:
        input_file = """
            Output file of the software tool. More information on the accepted format can 
            be found [here](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/)
            """

        pull_req = """
            It is open to the public indefinitely.
            """

        input_format = """
            Please select the software you used to generate the results. If it is not yet 
            implemented in ProteoBench, you can use a tab-delimited format that is described 
            further [here](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/)
        """

        parse_button = """
            Click here to see the output of your benchmark run
        """

        meta_data_file = """
            Please add a file with meta data that contains all relevant information about 
            your search parameters. See [here](https://proteobench.readthedocs.io/en/latest/modules/3-DDA-Quantification-ion-level/)
            for all compatible parameter files.
        """


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    StreamlitUI()
