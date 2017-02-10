
import model
m = model.Model([300,300],[100,50],dropout=0.5)

import multi_training
pcs = multi_training.loadPieces("music")

multi_training.trainPiece(m,pcs,10000)

#gen_adaptive(m,pcs,10,name="composition")