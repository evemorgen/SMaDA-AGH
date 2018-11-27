package net.sf.jclec.realarray.rec;
import org.apache.commons.lang.builder.EqualsBuilder;


public class MyDiscreteCrossover extends UniformCrossover2x2 {

    public MyDiscreteCrossover()
    {
        super();
    }

    @Override
    public boolean equals(Object other)
    {
        if (other instanceof DiscreteCrossover) {
            MyDiscreteCrossover o = (MyDiscreteCrossover) other;
            EqualsBuilder eb = new EqualsBuilder();
            eb.append(locusRecProb, o.locusRecProb);
            return eb.isEquals();
        }
        else {
            return false;
        }
    }

    @Override
    protected void recombineLocus(double[] p0_genome, double[] p1_genome, double[] s0_genome, double[] s1_genome, int locusIndex)
    {
        s0_genome[locusIndex] = Math.random() > 0.5 ? p1_genome[locusIndex] : p0_genome[locusIndex];
        s1_genome[locusIndex] = Math.random() > 0.5 ? p1_genome[locusIndex] : p0_genome[locusIndex];
    }

    @Override
    protected double defaultLocusRecProb() {
        return 0.6;
    }
}
