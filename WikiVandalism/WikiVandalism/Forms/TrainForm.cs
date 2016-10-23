using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace WikiVandalism
{
    public partial class TrainForm : Form
    {
        public TrainForm()
        {
            InitializeComponent();
        }

        private void LoadCLFBtn_Click(object sender, EventArgs e)
        {
            string result = MainForm.RunPythonScript("Scripts/test_all.py", "");
            Console.WriteLine("Python Result : " + result);

            ResultData data = JsonConvert.DeserializeObject<ResultData>(result);

            LRAcc.Text = data.lr + "%";
            KNNAcc.Text = data.knn + "%";
            AdaAcc.Text = data.adaboost + "%";
            NBAcc.Text = data.gnb + "%";
            SVMAcc.Text = data.svm + "%";
            GBTAcc.Text = data.gbt + "%";
            BNBAcc.Text = data.bnb + "%";
            RFAcc.Text = data.rf + "%";
            ETAcc.Text = data.et + "%";

            // Color the best - GBT
            GBTAcc.BackColor = Color.Green;
            GBTAcc.ForeColor = Color.White;

            LRR.Text = data.lrR + "%";
            KNNR.Text = data.knnR + "%";
            AdaR.Text = data.adaboostR + "%";
            NBR.Text = data.gnbR + "%";
            SVMR.Text = data.svmR + "%";
            GBTR.Text = data.gbtR + "%";
            BNBR.Text = data.bnbR + "%";
            RFR.Text = data.rfR + "%";
            ETR.Text = data.etR + "%";

            // Color the best - GBT
            GBTR.BackColor = Color.Green;
            GBTR.ForeColor = Color.White;

        }

        private class ResultData
        {
            public double adaboost;
            public double bnb;
            public double gnb;
            public double et;
            public double knn;
            public double lr;
            public double rf;
            public double svm;
            public double gbt;
            public double adaboostR;
            public double bnbR;
            public double gnbR;
            public double etR;
            public double knnR;
            public double lrR;
            public double rfR;
            public double svmR;
            public double gbtR;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MainForm f = new MainForm();
            f.Show();
            this.Hide();
        }

        private void TrainForm_Load(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }


    }
}
