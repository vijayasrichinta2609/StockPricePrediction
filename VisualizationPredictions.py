plt.plot(data.index[len(y_test):], y_test, label='Actual Prices', color='skyblue' ) 
plt.plot(data.index[len(y_test) :], y_pred, label='Predicted Prices', color='lightpink', linestyle='dashed')
plt.xlabel ('Time' )
plt.ylabel ('Stock Price Movement' )
plt.title('Actual vs. Predicted Stock Price Movements' )
plt. legend ()
plt.show()
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', map= 'Reds' )
plt.xlabel ('Predicted' )
plt.ylabel ('Actual')
plt.title('Confusion Matrix')
plt.show ()
fpr, tpr, thresholds_roc = roc_curve (y_test, y_prob) 
plt.plot(fpr, tpr, label='ROC Curve' )
plt.xlabel ('False Positive Rate' ) 
plt.ylabel ('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt. legend()
plt. show()
precision, recall, thresholds_pr = precision_recall_curve (y_test, y_prob) 
plt. plot (recall, precision, label='Precision-Recall Curve' ) 
plt.xlabel ('Recall' )|
plt.ylabel ('Precision')
plt.title ('Precision-Recall Curve' )
plt. legend ()
plt.show ()