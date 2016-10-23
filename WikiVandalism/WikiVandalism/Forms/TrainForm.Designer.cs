namespace WikiVandalism
{
    partial class TrainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.LoadCLFBtn = new System.Windows.Forms.Button();
            this.LRAcc = new System.Windows.Forms.Label();
            this.KNNAcc = new System.Windows.Forms.Label();
            this.AdaAcc = new System.Windows.Forms.Label();
            this.NBAcc = new System.Windows.Forms.Label();
            this.SVMAcc = new System.Windows.Forms.Label();
            this.GBTAcc = new System.Windows.Forms.Label();
            this.BNBAcc = new System.Windows.Forms.Label();
            this.RFAcc = new System.Windows.Forms.Label();
            this.ETAcc = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.label10 = new System.Windows.Forms.Label();
            this.AdaR = new System.Windows.Forms.Label();
            this.KNNR = new System.Windows.Forms.Label();
            this.LRR = new System.Windows.Forms.Label();
            this.GBTR = new System.Windows.Forms.Label();
            this.SVMR = new System.Windows.Forms.Label();
            this.NBR = new System.Windows.Forms.Label();
            this.ETR = new System.Windows.Forms.Label();
            this.RFR = new System.Windows.Forms.Label();
            this.BNBR = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(166, 137);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(132, 17);
            this.label1.TabIndex = 0;
            this.label1.Text = "Logistic Regression";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(166, 300);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(151, 17);
            this.label2.TabIndex = 1;
            this.label2.Text = "Gaussian Naive Bayes";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(166, 481);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(146, 17);
            this.label3.TabIndex = 2;
            this.label3.Text = "Bernoulli Naive Bayes";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(491, 137);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(140, 17);
            this.label4.TabIndex = 3;
            this.label4.Text = "k-Nearest Neighbour";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(491, 300);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(160, 17);
            this.label5.TabIndex = 4;
            this.label5.Text = "Support Vector Machine";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(491, 481);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(105, 17);
            this.label6.TabIndex = 5;
            this.label6.Text = "Random Forest";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(823, 137);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(69, 17);
            this.label7.TabIndex = 6;
            this.label7.Text = "AdaBoost";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(823, 300);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(156, 17);
            this.label8.TabIndex = 7;
            this.label8.Text = "Gradient Boosting Tree";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(823, 481);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(74, 17);
            this.label9.TabIndex = 8;
            this.label9.Text = "Extre Tree";
            // 
            // LoadCLFBtn
            // 
            this.LoadCLFBtn.BackColor = System.Drawing.Color.White;
            this.LoadCLFBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadCLFBtn.Location = new System.Drawing.Point(563, 676);
            this.LoadCLFBtn.Name = "LoadCLFBtn";
            this.LoadCLFBtn.Size = new System.Drawing.Size(180, 82);
            this.LoadCLFBtn.TabIndex = 9;
            this.LoadCLFBtn.Text = "Load Classifiers";
            this.LoadCLFBtn.UseVisualStyleBackColor = false;
            this.LoadCLFBtn.Click += new System.EventHandler(this.LoadCLFBtn_Click);
            // 
            // LRAcc
            // 
            this.LRAcc.AutoSize = true;
            this.LRAcc.BackColor = System.Drawing.Color.White;
            this.LRAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.LRAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LRAcc.Location = new System.Drawing.Point(169, 184);
            this.LRAcc.Name = "LRAcc";
            this.LRAcc.Size = new System.Drawing.Size(0, 25);
            this.LRAcc.TabIndex = 10;
            // 
            // KNNAcc
            // 
            this.KNNAcc.AutoSize = true;
            this.KNNAcc.BackColor = System.Drawing.Color.White;
            this.KNNAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.KNNAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.KNNAcc.Location = new System.Drawing.Point(489, 184);
            this.KNNAcc.Name = "KNNAcc";
            this.KNNAcc.Size = new System.Drawing.Size(0, 25);
            this.KNNAcc.TabIndex = 11;
            // 
            // AdaAcc
            // 
            this.AdaAcc.AutoSize = true;
            this.AdaAcc.BackColor = System.Drawing.Color.White;
            this.AdaAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.AdaAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.AdaAcc.Location = new System.Drawing.Point(821, 184);
            this.AdaAcc.Name = "AdaAcc";
            this.AdaAcc.Size = new System.Drawing.Size(0, 25);
            this.AdaAcc.TabIndex = 12;
            // 
            // NBAcc
            // 
            this.NBAcc.AutoSize = true;
            this.NBAcc.BackColor = System.Drawing.Color.White;
            this.NBAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.NBAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.NBAcc.Location = new System.Drawing.Point(164, 354);
            this.NBAcc.Name = "NBAcc";
            this.NBAcc.Size = new System.Drawing.Size(0, 25);
            this.NBAcc.TabIndex = 13;
            // 
            // SVMAcc
            // 
            this.SVMAcc.AutoSize = true;
            this.SVMAcc.BackColor = System.Drawing.Color.White;
            this.SVMAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.SVMAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SVMAcc.Location = new System.Drawing.Point(489, 354);
            this.SVMAcc.Name = "SVMAcc";
            this.SVMAcc.Size = new System.Drawing.Size(0, 25);
            this.SVMAcc.TabIndex = 14;
            // 
            // GBTAcc
            // 
            this.GBTAcc.AutoSize = true;
            this.GBTAcc.BackColor = System.Drawing.Color.White;
            this.GBTAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.GBTAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GBTAcc.Location = new System.Drawing.Point(821, 354);
            this.GBTAcc.Name = "GBTAcc";
            this.GBTAcc.Size = new System.Drawing.Size(0, 25);
            this.GBTAcc.TabIndex = 15;
            // 
            // BNBAcc
            // 
            this.BNBAcc.AutoSize = true;
            this.BNBAcc.BackColor = System.Drawing.Color.White;
            this.BNBAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.BNBAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BNBAcc.Location = new System.Drawing.Point(164, 538);
            this.BNBAcc.Name = "BNBAcc";
            this.BNBAcc.Size = new System.Drawing.Size(0, 25);
            this.BNBAcc.TabIndex = 16;
            // 
            // RFAcc
            // 
            this.RFAcc.AutoSize = true;
            this.RFAcc.BackColor = System.Drawing.Color.White;
            this.RFAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.RFAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RFAcc.Location = new System.Drawing.Point(489, 538);
            this.RFAcc.Name = "RFAcc";
            this.RFAcc.Size = new System.Drawing.Size(0, 25);
            this.RFAcc.TabIndex = 17;
            // 
            // ETAcc
            // 
            this.ETAcc.AutoSize = true;
            this.ETAcc.BackColor = System.Drawing.Color.White;
            this.ETAcc.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.ETAcc.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ETAcc.Location = new System.Drawing.Point(821, 538);
            this.ETAcc.Name = "ETAcc";
            this.ETAcc.Size = new System.Drawing.Size(0, 25);
            this.ETAcc.TabIndex = 18;
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.White;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(302, 676);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(182, 82);
            this.button1.TabIndex = 19;
            this.button1.Text = "Return";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label10.Location = new System.Drawing.Point(123, 39);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(823, 32);
            this.label10.TabIndex = 20;
            this.label10.Text = "Training of Models using Classical Machine Learning Algorithms";
            // 
            // AdaR
            // 
            this.AdaR.AutoSize = true;
            this.AdaR.BackColor = System.Drawing.Color.White;
            this.AdaR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.AdaR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.AdaR.Location = new System.Drawing.Point(821, 236);
            this.AdaR.Name = "AdaR";
            this.AdaR.Size = new System.Drawing.Size(0, 25);
            this.AdaR.TabIndex = 23;
            // 
            // KNNR
            // 
            this.KNNR.AutoSize = true;
            this.KNNR.BackColor = System.Drawing.Color.White;
            this.KNNR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.KNNR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.KNNR.Location = new System.Drawing.Point(489, 236);
            this.KNNR.Name = "KNNR";
            this.KNNR.Size = new System.Drawing.Size(0, 25);
            this.KNNR.TabIndex = 22;
            // 
            // LRR
            // 
            this.LRR.AutoSize = true;
            this.LRR.BackColor = System.Drawing.Color.White;
            this.LRR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.LRR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LRR.Location = new System.Drawing.Point(169, 236);
            this.LRR.Name = "LRR";
            this.LRR.Size = new System.Drawing.Size(0, 25);
            this.LRR.TabIndex = 21;
            // 
            // GBTR
            // 
            this.GBTR.AutoSize = true;
            this.GBTR.BackColor = System.Drawing.Color.White;
            this.GBTR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.GBTR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GBTR.Location = new System.Drawing.Point(816, 409);
            this.GBTR.Name = "GBTR";
            this.GBTR.Size = new System.Drawing.Size(0, 25);
            this.GBTR.TabIndex = 26;
            // 
            // SVMR
            // 
            this.SVMR.AutoSize = true;
            this.SVMR.BackColor = System.Drawing.Color.White;
            this.SVMR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.SVMR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SVMR.Location = new System.Drawing.Point(484, 409);
            this.SVMR.Name = "SVMR";
            this.SVMR.Size = new System.Drawing.Size(0, 25);
            this.SVMR.TabIndex = 25;
            // 
            // NBR
            // 
            this.NBR.AutoSize = true;
            this.NBR.BackColor = System.Drawing.Color.White;
            this.NBR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.NBR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.NBR.Location = new System.Drawing.Point(164, 409);
            this.NBR.Name = "NBR";
            this.NBR.Size = new System.Drawing.Size(0, 25);
            this.NBR.TabIndex = 24;
            // 
            // ETR
            // 
            this.ETR.AutoSize = true;
            this.ETR.BackColor = System.Drawing.Color.White;
            this.ETR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.ETR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ETR.Location = new System.Drawing.Point(816, 593);
            this.ETR.Name = "ETR";
            this.ETR.Size = new System.Drawing.Size(0, 25);
            this.ETR.TabIndex = 29;
            // 
            // RFR
            // 
            this.RFR.AutoSize = true;
            this.RFR.BackColor = System.Drawing.Color.White;
            this.RFR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.RFR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RFR.Location = new System.Drawing.Point(484, 593);
            this.RFR.Name = "RFR";
            this.RFR.Size = new System.Drawing.Size(0, 25);
            this.RFR.TabIndex = 28;
            // 
            // BNBR
            // 
            this.BNBR.AutoSize = true;
            this.BNBR.BackColor = System.Drawing.Color.White;
            this.BNBR.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.BNBR.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BNBR.Location = new System.Drawing.Point(164, 593);
            this.BNBR.Name = "BNBR";
            this.BNBR.Size = new System.Drawing.Size(0, 25);
            this.BNBR.TabIndex = 27;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(44, 184);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(66, 17);
            this.label11.TabIndex = 30;
            this.label11.Text = "Accuracy";
            this.label11.Click += new System.EventHandler(this.label11_Click);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(44, 244);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(71, 17);
            this.label12.TabIndex = 31;
            this.label12.Text = "ROC-AUC";
            this.label12.Click += new System.EventHandler(this.label12_Click);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(44, 414);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(71, 17);
            this.label13.TabIndex = 33;
            this.label13.Text = "ROC-AUC";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(44, 354);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(66, 17);
            this.label14.TabIndex = 32;
            this.label14.Text = "Accuracy";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(49, 598);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(71, 17);
            this.label15.TabIndex = 35;
            this.label15.Text = "ROC-AUC";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(49, 538);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(66, 17);
            this.label16.TabIndex = 34;
            this.label16.Text = "Accuracy";
            // 
            // TrainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1044, 770);
            this.Controls.Add(this.label15);
            this.Controls.Add(this.label16);
            this.Controls.Add(this.label13);
            this.Controls.Add(this.label14);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.ETR);
            this.Controls.Add(this.RFR);
            this.Controls.Add(this.BNBR);
            this.Controls.Add(this.GBTR);
            this.Controls.Add(this.SVMR);
            this.Controls.Add(this.NBR);
            this.Controls.Add(this.AdaR);
            this.Controls.Add(this.KNNR);
            this.Controls.Add(this.LRR);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.ETAcc);
            this.Controls.Add(this.RFAcc);
            this.Controls.Add(this.BNBAcc);
            this.Controls.Add(this.GBTAcc);
            this.Controls.Add(this.SVMAcc);
            this.Controls.Add(this.NBAcc);
            this.Controls.Add(this.AdaAcc);
            this.Controls.Add(this.KNNAcc);
            this.Controls.Add(this.LRAcc);
            this.Controls.Add(this.LoadCLFBtn);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "TrainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Warning System for Vandalism Detection in Wikipedia";
            this.Load += new System.EventHandler(this.TrainForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Button LoadCLFBtn;
        private System.Windows.Forms.Label LRAcc;
        private System.Windows.Forms.Label KNNAcc;
        private System.Windows.Forms.Label AdaAcc;
        private System.Windows.Forms.Label NBAcc;
        private System.Windows.Forms.Label SVMAcc;
        private System.Windows.Forms.Label GBTAcc;
        private System.Windows.Forms.Label BNBAcc;
        private System.Windows.Forms.Label RFAcc;
        private System.Windows.Forms.Label ETAcc;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label AdaR;
        private System.Windows.Forms.Label KNNR;
        private System.Windows.Forms.Label LRR;
        private System.Windows.Forms.Label GBTR;
        private System.Windows.Forms.Label SVMR;
        private System.Windows.Forms.Label NBR;
        private System.Windows.Forms.Label ETR;
        private System.Windows.Forms.Label RFR;
        private System.Windows.Forms.Label BNBR;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label16;
    }
}