import numpy as np

from group_stratifier import GroupStratifiedKFold

n_samples = 100000
n_classes = 10
n_classes2 = 20
n_splits = 4
n_groups = 1000

rng = np.random.RandomState(7)
stratifier = GroupStratifiedKFold(n_splits=n_splits, random_state=12, population_size=200, generations=10)
labels1 = rng.randint(0, n_classes, n_samples, dtype=np.int32)
labels2 = rng.randint(0, n_classes2, n_samples, dtype=np.int32)
labels = np.stack((labels1, labels2))
groups = rng.randint(0, n_groups, n_samples, dtype=np.int32)
fitness, folds = stratifier.split(labels, groups)
print(fitness)
print(folds)
